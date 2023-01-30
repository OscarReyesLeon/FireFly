from django.http import HttpResponse, JsonResponse
from .forms import ReportSensorForm, ReportSensorMForm
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Avg
from .models import LecturaModel
import pandas as pd
import numpy as np
from django.contrib.auth.decorators import login_required, permission_required

# from dateutil.rrule import rrule, MONTHLY, YEARLY, WEEKLY, DAILY, HOURLY
def get_values(request):
    fecha_inicial = request.POST.get('fecha_inicial', timezone.now().strftime('%Y-%m-%d'))
    fecha_final = request.POST.get('fecha_final', timezone.now().strftime('%Y-%m-%d'))
    fecha_inicial = timezone.datetime.strptime(fecha_inicial, '%Y-%m-%d')
    fecha_final = timezone.datetime.strptime(fecha_final, '%Y-%m-%d')
    fecha_final = fecha_final.replace(hour=23, minute=59, second=59)
    maquina = request.POST.getlist('maquina[]', "")
    dict_filter = {
        'fecha__range': [fecha_inicial, fecha_final],
        'valor__gte': 3
    }

    if maquina:
        dict_filter.update({'maquina__in': maquina,})
    turno = request.POST.get('turno', '')
    dict_exclude = {}
    if turno:
        if turno == '1':
            hora_inicial, hora_final = 6, 12
        elif turno == '2':
            hora_inicial, hora_final = 13, 20 #condicion ""=="" (si termina a las 20:59 se pone las 20)
        elif turno == '4':
            hora_inicial, hora_final = 21, 21 #condicion ""=="" (si termina a las 20:59 se pone las 20)
        if turno == '3':
            dict_exclude.update({
                'fecha__hour__range': [6, 21], 
            }) #todo lo que no esté, condicional
        else:
            dict_filter.update({
                'fecha__hour__range': [hora_inicial, hora_final],
            })
    promedio = request.POST.get('promedio', 'Hora')
    if promedio == 'Anual':
        values = [ 'fecha__year']
    elif promedio == 'Mensual':
        values = ['fecha__month', 'fecha__year']
    elif promedio == 'Semanal':
        values = ['fecha__week', 'fecha__year']
    elif promedio == 'Diario':
        values = ['fecha__day', 'fecha__month', 'fecha__year']
    elif promedio == 'Hora':
        values = ['fecha__day', 'fecha__month', 'fecha__year', 'fecha__hour']
    if promedio == 'Minuto':
        values = ['fecha__day', 'fecha__month', 'fecha__year', 'fecha__hour', 'fecha__minute']

    values.append('maquina')
    return dict_filter, dict_exclude, values, promedio

@login_required(login_url='/login/')
@permission_required('prf.change_sundara', login_url='bases:sin_privilegios')
def report_sensor(request):
    if request.method == 'POST':
        dict_filter, dict_exclude, values, promedio = get_values(request)
        lectura = LecturaModel.objects.filter(**dict_filter).using('sensor') #
        if dict_exclude:
            lectura = lectura.exclude(**dict_exclude)
        machines = lectura.values('maquina', 'maquina__nombre').distinct()
        lectura = lectura.values(*values).annotate(valor=Avg('valor')).order_by(*values).distinct() #evita duplicados agrupando similares
        if not lectura:
            return JsonResponse('No hay datos para mostrar', status=404, safe=False)
        lectura_values = pd.DataFrame(list(lectura))
        print(lectura_values)
        values_by_machine = values[:-1]
        #Columna valor a dos decimales
        lectura_values['valor'] = lectura_values['valor'].round(0)
        lectura_values = lectura_values.pivot(index=values_by_machine, 
            columns='maquina', values='valor').reset_index()
        lectura_values.replace(np.nan, 0, inplace=True) 

        if promedio == 'Anual':
            lectura_values['Fecha'] = lectura_values['fecha__year'].astype(str)
        elif promedio == 'Mensual':
            lectura_values['Fecha'] = lectura_values['fecha__month'].astype(str) + '-' + lectura_values['fecha__year'].astype(str)
        elif promedio == 'Semanal':
            lectura_values['Fecha'] = lectura_values['fecha__week'].astype(str) + '-' + lectura_values['fecha__year'].astype(str)
        elif promedio in ['Diario', 'Hora', 'Minuto']:
            lectura_values['Fecha'] = lectura_values['fecha__day'].astype(str) + '-' + lectura_values['fecha__month'].astype(str) + '-' + lectura_values['fecha__year'].astype(str)

        orden_filas = ['Fecha']
        ordenar_por = ["Fecha"]
        restar_columna = 0
        if "fecha__hour" in lectura_values.columns:
            orden_filas.append("Hora")
            ordenar_por.append("Hora")
            restar_columna += 1
        if "fecha__minute" in lectura_values.columns:
            orden_filas.append("Minuto")
            ordenar_por.append("Minuto")
            restar_columna += 1

        sobreescribir_nombre_columnas = {
            "fecha__hour": "Hora",
            "fecha__minute": "Minuto"
        }

        for mach in machines:
            sobreescribir_nombre_columnas.update({mach['maquina']: mach['maquina__nombre']}) #cambia ID por nombre de maquina
            orden_filas.append(mach['maquina__nombre'])

        if promedio in ['Hora', 'Minuto']:
            values_by_machine = values_by_machine[:-restar_columna]
        lectura_values.drop(values_by_machine, axis=1,inplace=True)
        lectura_values.rename(columns = sobreescribir_nombre_columnas, inplace = True)

        lectura_values = lectura_values[orden_filas]
        lectura_values.sort_values(by=ordenar_por, inplace=True, ascending=False)
        export_report = request.POST.get('export_report', 'false')
        if export_report in ['1','true']:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=category.csv'
            lectura_values.to_csv(path_or_buf=response)
            return response
        lectura_values_dict = lectura_values.to_dict('records')
        return JsonResponse(lectura_values_dict, safe=False)
    else:
        form = ReportSensorMForm()
        return render(request, 'report_sensor.html', {'form': form})
@login_required(login_url='/login/')
@permission_required('prf.change_sundara', login_url='bases:sin_privilegios')
def get_valuesc(request):
    fecha_inicial = request.POST.get('fecha_inicial', timezone.now().strftime('%Y-%m-%d'))
    fecha_final = request.POST.get('fecha_final', timezone.now().strftime('%Y-%m-%d'))
    fecha_inicial = timezone.datetime.strptime(fecha_inicial, '%Y-%m-%d')
    fecha_final = timezone.datetime.strptime(fecha_final, '%Y-%m-%d')
    fecha_final = fecha_final.replace(hour=23, minute=59, second=59)
    maquina = request.POST.getlist('maquina[]', "")
    dict_filter = {
        'fecha__range': [fecha_inicial, fecha_final],
    }

    if maquina:
        dict_filter.update({'maquina__in': maquina,})
    turno = request.POST.get('turno', '')
    dict_exclude = {}
    if turno:
        if turno == '1':
            hora_inicial, hora_final = 6, 12
        elif turno == '2':
            hora_inicial, hora_final = 13, 20
        if turno == '3':
            dict_exclude.update({
                'fecha__hour__range': [6, 21],
            })
        else:
            dict_filter.update({
                'fecha__hour__range': [hora_inicial, hora_final],
            })
    promedio = request.POST.get('promedio', 'Hora')
    if promedio == 'Anual':
        values = [ 'fecha__year']
    elif promedio == 'Mensual':
        values = ['fecha__month', 'fecha__year']
    elif promedio == 'Semanal':
        values = ['fecha__week', 'fecha__year']
    elif promedio == 'Diario':
        values = ['fecha__day', 'fecha__month', 'fecha__year']
    if promedio == 'Hora':
        values = ['fecha__day', 'fecha__month', 'fecha__year', 'fecha__hour']
    values.append('maquina')
    return dict_filter, dict_exclude, values, promedio

@login_required(login_url='/login/')
@permission_required('prf.change_sundara', login_url='bases:sin_privilegios')
def report_remplazo(request):
    if request.method == 'POST':
        dict_filter, dict_exclude, values, promedio = get_valuesc(request)
        lectura = LecturaModel.objects.filter(**dict_filter).using('sensor')
        if dict_exclude:
            lectura = lectura.exclude(**dict_exclude)
        machines = lectura.values('maquina', 'maquina__nombre').distinct()
        lectura = lectura.values(*values).annotate(valor=Avg('valor')).order_by(*values).distinct()
        if not lectura:
            return JsonResponse('No hay datos para mostrar', status=404, safe=False)
        lectura_values = pd.DataFrame(list(lectura))
        values_by_machine = values[:-1]
        #Columna valor a dos decimales
        lectura_temporal = lectura_values['valor'].round(0)
        for index, value in enumerate(lectura_temporal):
            if value <= 3:
                lectura_temporal[index] = 0
        lectura_values['valor'] = lectura_temporal
        lectura_values = lectura_values.pivot(index=values_by_machine,
            columns='maquina', values='valor').reset_index()
        lectura_values.replace(np.nan, 0, inplace=True)

        if promedio == 'Anual':
            lectura_values['Fecha'] = lectura_values['fecha__year'].astype(str)
        elif promedio == 'Mensual':
            lectura_values['Fecha'] = lectura_values['fecha__month'].astype(str) + '-' + lectura_values['fecha__year'].astype(str)
        elif promedio == 'Semanal':
            lectura_values['Fecha'] = lectura_values['fecha__week'].astype(str) + '-' + lectura_values['fecha__year'].astype(str)
        elif promedio in ['Diario', 'Hora']:
            lectura_values['Fecha'] = lectura_values['fecha__day'].astype(str) + '-' + lectura_values['fecha__month'].astype(str) + '-' + lectura_values['fecha__year'].astype(str)

        orden_filas = ['Fecha']
        ordenar_por = ["Fecha"]
        if "fecha__hour" in lectura_values.columns:
            orden_filas.append("Hora")
            ordenar_por.append("Hora")

        sobreescribir_nombre_columnas = {
            "fecha__hour": "Hora"
        }

        for mach in machines:
            sobreescribir_nombre_columnas.update({mach['maquina']: mach['maquina__nombre']})
            orden_filas.append(mach['maquina__nombre'])

        if promedio == "Hora":
            values_by_machine = values_by_machine[:-1]
        lectura_values.drop(values_by_machine, axis=1,inplace=True)
        lectura_values.rename(columns = sobreescribir_nombre_columnas, inplace = True)

        lectura_values = lectura_values[orden_filas]
        lectura_values.sort_values(by=ordenar_por, inplace=True, ascending=False)
        export_report = request.POST.get('export_report', 'false')
        if export_report in ['1','true']:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=category.csv'
            lectura_values.to_csv(path_or_buf=response)
            return response
        lectura_values_dict = lectura_values.to_dict('records')
        return JsonResponse(lectura_values_dict, safe=False)

    else:
        form = ReportSensorForm()
        return render(request, 'report_remplazo.html', {'form': form})

@login_required(login_url='/login/')
@permission_required('prf.change_sundara', login_url='bases:sin_privilegios')
def report_crudo(request):
    if request.method == 'POST':
        dict_filter, dict_exclude, values, promedio = get_valuesc(request)
        lectura = LecturaModel.objects.filter(**dict_filter).using('sensor')
        if dict_exclude:
            lectura = lectura.exclude(**dict_exclude)
        machines = lectura.values('maquina', 'maquina__nombre').distinct()
        lectura = lectura.values(*values).annotate(valor=Avg('valor')).order_by(*values).distinct()
        if not lectura:
            return JsonResponse('No hay datos para mostrar', status=404, safe=False)
        lectura_values = pd.DataFrame(list(lectura))
        values_by_machine = values[:-1]
        #Columna valor a dos decimales
        lectura_values['valor'] = lectura_values['valor']
        lectura_values = lectura_values.pivot(index=values_by_machine, 
            columns='maquina', values='valor').reset_index()
        lectura_values.replace(np.nan, 0, inplace=True) 

        if promedio == 'Anual':
            lectura_values['Fecha'] = lectura_values['fecha__year'].astype(str)
        elif promedio == 'Mensual':
            lectura_values['Fecha'] = lectura_values['fecha__month'].astype(str) + '-' + lectura_values['fecha__year'].astype(str)
        elif promedio == 'Semanal':
            lectura_values['Fecha'] = lectura_values['fecha__week'].astype(str) + '-' + lectura_values['fecha__year'].astype(str)
        elif promedio in ['Diario', 'Hora']:
            lectura_values['Fecha'] = lectura_values['fecha__day'].astype(str) + '-' + lectura_values['fecha__month'].astype(str) + '-' + lectura_values['fecha__year'].astype(str)

        orden_filas = ['Fecha']
        ordenar_por = ["Fecha"]
        if "fecha__hour" in lectura_values.columns:
            orden_filas.append("Hora")
            ordenar_por.append("Hora")

        sobreescribir_nombre_columnas = {
            "fecha__hour": "Hora"
        }

        for mach in machines:
            sobreescribir_nombre_columnas.update({mach['maquina']: mach['maquina__nombre']})
            orden_filas.append(mach['maquina__nombre'])

        if promedio == "Hora":
            values_by_machine = values_by_machine[:-1]
        lectura_values.drop(values_by_machine, axis=1,inplace=True)
        lectura_values.rename(columns = sobreescribir_nombre_columnas, inplace = True)

        lectura_values = lectura_values[orden_filas]
        lectura_values.sort_values(by=ordenar_por, inplace=True, ascending=False)
        export_report = request.POST.get('export_report', 'false')
        if export_report in ['1','true']:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=category.csv'
            lectura_values.to_csv(path_or_buf=response)
            return response
        lectura_values_dict = lectura_values.to_dict('records')
        return JsonResponse(lectura_values_dict, safe=False)

    else:
        form = ReportSensorForm()
        return render(request, 'report_crudo.html', {'form': form})