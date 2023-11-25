from django.http import HttpResponse, JsonResponse
from .forms import ReportSensorForm, ReportSensorMForm
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Avg
from .models import LecturaModel, MaquinaModel
import pandas as pd
import numpy as np
from django.contrib.auth.decorators import login_required, permission_required
import time
from django.core.cache import cache


# from dateutil.rrule import rrule, MONTHLY, YEARLY, WEEKLY, DAILY, HOURLY
def process_sensor(request):
    fecha_inicial = request.POST.get(
        "fecha_inicial", timezone.now().strftime("%Y-%m-%d")
    )
    fecha_final = request.POST.get("fecha_final", timezone.now().strftime("%Y-%m-%d"))
    fecha_inicial = timezone.datetime.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_final = timezone.datetime.strptime(fecha_final, "%Y-%m-%d")
    fecha_final = fecha_final.replace(hour=23, minute=59, second=59)
    maquina = request.POST.getlist("maquina[]", "")
    dict_filter = {
        "fecha__range": [fecha_inicial, fecha_final],
    }
    if maquina:
        dict_filter.update(
            {
                "maquina__in": maquina,
            }
        )
    lectura = (
        LecturaModel.objects.filter(**dict_filter)
        .using("sensor")
        .values("fecha", "maquina", "maquina__nombre", "valor")
    )
    lectura_values = pd.DataFrame(list(lectura))
    lectura_values["Fecha"] = lectura_values["fecha"].dt.date
    promedio = request.POST.get("promedio", "Hora")
    if promedio == "Anual":
        lectura_values["Año"] = lectura_values["fecha"].dt.year
        extra_group = ["Año"]
        order_by = ["Año"]
    elif promedio == "Mensual":
        lectura_values["Año"] = lectura_values["fecha"].dt.year
        lectura_values["Mes"] = lectura_values["fecha"].dt.month
        extra_group = ["Mes", "Año"]
        order_by = ["Mes", "Año"]
    elif promedio == "Diario":
        extra_group = ["Fecha"]
        order_by = ["Fecha"]
    elif promedio == "Hora":
        lectura_values["Año"] = lectura_values["fecha"].dt.year
        lectura_values["Mes"] = lectura_values["fecha"].dt.month
        lectura_values["Dia"] = lectura_values["fecha"].dt.day
        lectura_values["Hora"] = lectura_values["fecha"].dt.hour
        extra_group = ["Hora", "Fecha"]
        order_by = ["Hora"]
    elif promedio == "Minuto":
        lectura_values["Hora"] = lectura_values["fecha"].dt.hour
        lectura_values["Minuto"] = lectura_values["fecha"].dt.minute
        extra_group = ["Minuto", "Hora", "Fecha"]
        order_by = ["Fecha", "Hora", "Minuto"]

    # Copiar maquina__nombre a maquina
    lectura_values["maquina"] = lectura_values["maquina__nombre"]
    lectura2 = (
        lectura_values.groupby(
            [
                "maquina",
            ]
            + extra_group
        )["valor"]
        .mean()
        .unstack("maquina")
        .fillna(0)
        .round(2)
        .reset_index()
    )
    columnas = lectura2.columns.tolist()
    lectura2 = lectura2.sort_values(by=order_by, ascending=False)
    lectura2["Fecha"] = lectura2["Fecha"].astype(str)
    for i in range(0, len(order_by)):
        columnas.insert(i, columnas.pop(columnas.index(order_by[i])))
    export_report = request.POST.get("export_report", "false")
    if export_report in ["1", "true"]:
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=category.csv"
        lectura_values.to_csv(path_or_buf=response)
        return response
    return JsonResponse(lectura2[columnas].to_dict("records"), safe=False)


@login_required(login_url="/login/")
@permission_required("prf.change_sundara", login_url="bases:sin_privilegios")
def report_sensor(request):
    if request.method == "POST":
        return process_sensor(request)
    else:
        form = ReportSensorMForm()
        return render(request, "report_sensor.html", {"form": form})


@login_required(login_url="/login/")
@permission_required("prf.change_sundara", login_url="bases:sin_privilegios")
def get_valuesc(request):
    fecha_inicial = request.POST.get(
        "fecha_inicial", timezone.now().strftime("%Y-%m-%d")
    )
    fecha_final = request.POST.get("fecha_final", timezone.now().strftime("%Y-%m-%d"))
    fecha_inicial = timezone.datetime.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_final = timezone.datetime.strptime(fecha_final, "%Y-%m-%d")
    fecha_final = fecha_final.replace(hour=23, minute=59, second=59)
    maquina = request.POST.getlist("maquina[]", "")
    dict_filter = {
        "fecha__range": [fecha_inicial, fecha_final],
    }

    if maquina:
        dict_filter.update(
            {
                "maquina__in": maquina,
            }
        )
    turno = request.POST.get("turno", "")
    dict_exclude = {}
    if turno:
        if turno == "1":
            hora_inicial, hora_final = 6, 12
        elif turno == "2":
            hora_inicial, hora_final = 13, 20
        if turno == "3":
            dict_exclude.update(
                {
                    "fecha__hour__range": [6, 21],
                }
            )
        else:
            dict_filter.update(
                {
                    "fecha__hour__range": [hora_inicial, hora_final],
                }
            )
    promedio = request.POST.get("promedio", "Hora")
    if promedio == "Anual":
        values = ["fecha__year"]
    elif promedio == "Mensual":
        values = ["fecha__month", "fecha__year"]
    elif promedio == "Semanal":
        values = ["fecha__week", "fecha__year"]
    elif promedio == "Diario":
        values = ["fecha__day", "fecha__month", "fecha__year"]
    if promedio == "Hora":
        values = ["fecha__day", "fecha__month", "fecha__year", "fecha__hour"]
    values.append("maquina")
    return dict_filter, dict_exclude, values, promedio


@login_required(login_url="/login/")
@permission_required("prf.change_sundara", login_url="bases:sin_privilegios")
def report_remplazo(request):
    if request.method == "POST":
        dict_filter, dict_exclude, values, promedio = get_valuesc(request)
        lectura = LecturaModel.objects.filter(**dict_filter).using("sensor")
        if dict_exclude:
            lectura = lectura.exclude(**dict_exclude)
        machines = lectura.values("maquina", "maquina__nombre").distinct()
        lectura = (
            lectura.values(*values)
            .annotate(valor=Avg("valor"))
            .order_by(*values)
            .distinct()
        )
        if not lectura:
            return JsonResponse("No hay datos para mostrar", status=404, safe=False)
        lectura_values = pd.DataFrame(list(lectura))
        values_by_machine = values[:-1]
        # Columna valor a dos decimales
        lectura_temporal = lectura_values["valor"].round(0)
        for index, value in enumerate(lectura_temporal):
            if value <= 3:
                lectura_temporal[index] = 0
        lectura_values["valor"] = lectura_temporal
        lectura_values = lectura_values.pivot(
            index=values_by_machine, columns="maquina", values="valor"
        ).reset_index()
        lectura_values.replace(np.nan, 0, inplace=True)

        if promedio == "Anual":
            lectura_values["Fecha"] = lectura_values["fecha__year"].astype(str)
        elif promedio == "Mensual":
            lectura_values["Fecha"] = (
                lectura_values["fecha__month"].astype(str)
                + "-"
                + lectura_values["fecha__year"].astype(str)
            )
        elif promedio == "Semanal":
            lectura_values["Fecha"] = (
                lectura_values["fecha__week"].astype(str)
                + "-"
                + lectura_values["fecha__year"].astype(str)
            )
        elif promedio in ["Diario", "Hora"]:
            lectura_values["Fecha"] = (
                lectura_values["fecha__day"].astype(str)
                + "-"
                + lectura_values["fecha__month"].astype(str)
                + "-"
                + lectura_values["fecha__year"].astype(str)
            )

        orden_filas = ["Fecha"]
        ordenar_por = ["Fecha"]
        if "fecha__hour" in lectura_values.columns:
            orden_filas.append("Hora")
            ordenar_por.append("Hora")

        sobreescribir_nombre_columnas = {"fecha__hour": "Hora"}

        for mach in machines:
            sobreescribir_nombre_columnas.update(
                {mach["maquina"]: mach["maquina__nombre"]}
            )
            orden_filas.append(mach["maquina__nombre"])

        if promedio == "Hora":
            values_by_machine = values_by_machine[:-1]
        lectura_values.drop(values_by_machine, axis=1, inplace=True)
        lectura_values.rename(columns=sobreescribir_nombre_columnas, inplace=True)

        lectura_values = lectura_values[orden_filas]
        lectura_values.sort_values(by=ordenar_por, inplace=True, ascending=False)
        export_report = request.POST.get("export_report", "false")
        if export_report in ["1", "true"]:
            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = "attachment; filename=category.csv"
            lectura_values.to_csv(path_or_buf=response)
            return response
        lectura_values_dict = lectura_values.to_dict("records")
        return JsonResponse(lectura_values_dict, safe=False)

    else:
        form = ReportSensorForm()
        return render(request, "report_remplazo.html", {"form": form})


@login_required(login_url="/login/")
@permission_required("prf.change_sundara", login_url="bases:sin_privilegios")
def report_crudo(request):
    if request.method == "POST":
        dict_filter, dict_exclude, values, promedio = get_valuesc(request)
        lectura = LecturaModel.objects.filter(**dict_filter).using("sensor")
        if dict_exclude:
            lectura = lectura.exclude(**dict_exclude)
        machines = lectura.values("maquina", "maquina__nombre").distinct()
        lectura = (
            lectura.values(*values)
            .annotate(valor=Avg("valor"))
            .order_by(*values)
            .distinct()
        )
        if not lectura:
            return JsonResponse("No hay datos para mostrar", status=404, safe=False)
        lectura_values = pd.DataFrame(list(lectura))
        values_by_machine = values[:-1]
        # Columna valor a dos decimales
        lectura_values["valor"] = lectura_values["valor"]
        lectura_values = lectura_values.pivot(
            index=values_by_machine, columns="maquina", values="valor"
        ).reset_index()
        lectura_values.replace(np.nan, 0, inplace=True)

        if promedio == "Anual":
            lectura_values["Fecha"] = lectura_values["fecha__year"].astype(str)
        elif promedio == "Mensual":
            lectura_values["Fecha"] = (
                lectura_values["fecha__month"].astype(str)
                + "-"
                + lectura_values["fecha__year"].astype(str)
            )
        elif promedio == "Semanal":
            lectura_values["Fecha"] = (
                lectura_values["fecha__week"].astype(str)
                + "-"
                + lectura_values["fecha__year"].astype(str)
            )
        elif promedio in ["Diario", "Hora"]:
            lectura_values["Fecha"] = (
                lectura_values["fecha__day"].astype(str)
                + "-"
                + lectura_values["fecha__month"].astype(str)
                + "-"
                + lectura_values["fecha__year"].astype(str)
            )

        orden_filas = ["Fecha"]
        ordenar_por = ["Fecha"]
        if "fecha__hour" in lectura_values.columns:
            orden_filas.append("Hora")
            ordenar_por.append("Hora")

        sobreescribir_nombre_columnas = {"fecha__hour": "Hora"}

        for mach in machines:
            sobreescribir_nombre_columnas.update(
                {mach["maquina"]: mach["maquina__nombre"]}
            )
            orden_filas.append(mach["maquina__nombre"])

        if promedio == "Hora":
            values_by_machine = values_by_machine[:-1]
        lectura_values.drop(values_by_machine, axis=1, inplace=True)
        lectura_values.rename(columns=sobreescribir_nombre_columnas, inplace=True)

        lectura_values = lectura_values[orden_filas]
        lectura_values.sort_values(by=ordenar_por, inplace=True, ascending=False)
        export_report = request.POST.get("export_report", "false")
        if export_report in ["1", "true"]:
            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = "attachment; filename=category.csv"
            lectura_values.to_csv(path_or_buf=response)
            return response
        lectura_values_dict = lectura_values.to_dict("records")
        return JsonResponse(lectura_values_dict, safe=False)

    else:
        form = ReportSensorForm()
        return render(request, "report_crudo.html", {"form": form})


@login_required(login_url="/login/")
@permission_required("prf.change_sundara", login_url="bases:sin_privilegios")
def report_status_sensor(request):
    """
    La salida de sundara, procesar y mostrar en la vista
    Reporte que de la última semana por default (7 días) y que se pueda seleccionar el rango de fechas

    Cache de cada 30 minutos
    Navegador con auto refresh de cada 5 minutos
    Navegador a pantalla completa

    1- Obtener los datos entre 2 fechas
    2- Encontrar el cambio de 0 a 10 de voltaje, eso indica que se encendió la máquina
    3- Encontrar el cambio de 10 a 0 de voltaje, eso indica que se apagó la máquina
    4- Calcular el tiempo que estuvo encendida la máquina
    5- Calcular el voltaje promedio de la máquina encendida
    6- Calcular el tiempo que estuvo apagada la máquina antes de volver a encenderse
    7- Encontrar el siguiente cambio de 0 a 10 de voltaje, eso indica que se encendió la máquina
    8- Repetir el proceso hasta que se acaben los datos
    """

    if request.is_ajax():
        cache_key = "report_status_sensor"
        cache_time = 30 * 60
        try:
            from apps.external.services.dashboard_report import DashboardService

            data = cache.get(cache_key)
            if not data:
                instance = DashboardService(hours=24)
                data = instance.process_dashboard()
                # data = MI_DATA
                cache.set(cache_key, data, cache_time)
            return JsonResponse(data, safe=False, status=200)
        except Exception as e:
            print(str(e))
            raise e

    return render(request, "report_status_sensor.html", {})
