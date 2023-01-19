from django.http import HttpResponse, JsonResponse
from .forms import ReportSensorForm
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Avg
from .models import LecturaModel
import pandas as pd
import numpy as np
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
    }
    if maquina:
        dict_filter.update({'maquina__in': maquina,})
    hora_inicial = request.POST.get('hora_inicial', '00:00').split(':')
    hora_final = request.POST.get('hora_final', '23:59').split(':')
    dict_filter.update({
        'fecha__hour__range': [hora_inicial[0], hora_final[0]],
        'fecha__minute__range': [hora_inicial[1], hora_final[1]],
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
        values = ['fecha__year', 'fecha__month', 'fecha__day', 'fecha__hour']
    values.append('maquina')
    return dict_filter, values, promedio

def report_sensor(request):
    if request.method == 'POST':
        dict_filter, values, promedio = get_values(request)
        lectura = LecturaModel.objects.filter(**dict_filter).using('sensor')
        machines = lectura.values('maquina', 'maquina__nombre').distinct()
        lectura = lectura.values(*values).annotate(valor=Avg('valor')).order_by(
            *["-{}".format(v) for v in values]
        ).distinct()
        lectura_values = pd.DataFrame(list(lectura))
        values_by_machine = values[:-1]
        #Columna valor a dos decimales
        lectura_values['valor'] = lectura_values['valor'].round(2)
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
        return render(request, 'report_sensor.html', {'form': form})