from .models import MaquinaModel
from django.utils import timezone
from django import forms
class ReportSensorForm(forms.Form):
    promedio = forms.ChoiceField(
        choices=[
            ('Hora', 'Hora'),
            ('Diario', 'Diario'),
            ('Semanal', 'Semanal'),
            ('Mensual', 'Mensual'),
            ('Anual', 'Anual'),
        ],
        initial='Anual',
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Agrupar por'
    )
    maquina = forms.ModelMultipleChoiceField(
        queryset=MaquinaModel.objects.all().using('sensor').order_by('nombre'),
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2'})
    )
    fecha_inicial = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'value': timezone.now().strftime('%Y-%m-%d') })
    )
    hora_inicial = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'value': '00:00', 'min': '00:00', 'max': '23:59', 'step': '1'})
    )
    fecha_final = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'value': timezone.now().strftime('%Y-%m-%d')})
    )
    hora_final = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'value': '23:59', 'min': '00:00', 'max': '23:59', 'step': '1'})
    )