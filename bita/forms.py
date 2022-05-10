from django import forms

from .models import *

class OperadorPesadoForm(forms.ModelForm):
    class Meta:
        model=OperadorPesado
        exclude = ['um', 'fm', 'uc', 'fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':"form-control"})
class SolicitantesUtilitarioForm(forms.ModelForm):
    class Meta:
        model=SolicitantesUtilitario
        exclude = ['um', 'fm', 'uc', 'fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':"form-control"})

class VehiculoLigeroForm(forms.ModelForm):
    class Meta:
        model=VehiculoLigero
        exclude = ['um', 'fm', 'uc', 'fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':"form-control"})

class VehiculoPesadoForm(forms.ModelForm):
    class Meta:
        model=VehiculoPesado
        exclude = ['um', 'fm', 'uc', 'fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':"form-control"})

class MotivoIngresoUnidadForm(forms.ModelForm):
    class Meta:
        model=MotivoIngresoUnidad
        exclude = ['um', 'fm', 'uc', 'fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':"form-control"})

class DestinosClientesForm(forms.ModelForm):
    class Meta:
        model=DestinosClientes
        exclude = ['um', 'fm', 'uc', 'fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':"form-control"})

class MotivoVisitaForm(forms.ModelForm):
    class Meta:
        model=MotivoVisita
        exclude = ['um', 'fm', 'uc', 'fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':"form-control"})
class CargaDeUreaForm(forms.ModelForm):
    class Meta:
        model=CargaDeUrea
        exclude = ['um', 'fm', 'uc', 'fc', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':"form-control"})

class TanquesDieselForm(forms.ModelForm):
    class Meta:
        model=TanquesDiesel
        exclude = ['um', 'fm', 'uc', 'fc', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':"form-control"})
class DescargaDeDieselForm(forms.ModelForm):
    pedido = forms.ModelChoiceField(queryset=Pedido.objects.filter(UniMed_id=5).order_by('-id')[:20])
    class Meta:
        model=DescargaDeDiesel
        exclude = ['um', 'fm', 'uc', 'fc', 'estado', 'residual']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':"form-control"})
""
class CargaDeDieselForm(forms.ModelForm):
    class Meta:
        model=CargaDeDiesel
        exclude = ['um', 'fm', 'uc', 'fc', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['destino'].widget.attrs['class'] = 'form-control select2'
        self.fields['vehiculo'].widget.attrs['class'] = 'form-control select2'

    
class IngresoUnidadPesadaForm(forms.ModelForm):
    class Meta:
        model=IngresoUnidadPesada
        exclude = ['um', 'fm', 'uc', 'fc', 'fsalida', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':"form-control"})
