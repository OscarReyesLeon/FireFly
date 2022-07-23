from django import forms

from .models import Proveedor, ComprasEnc, UsoFactura

class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        exclude = ['um','fm','uc','fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['cuentabanco'].widget.attrs['readonly'] = True



    def clean(self):
        try:
            sc = Proveedor.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk!=sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Proveedor.DoesNotExist:
            pass
        return self.cleaned_data
class UsoFacturaForm(forms.ModelForm):
    class Meta:
        model=UsoFactura
        exclude = ['um','fm','uc','fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


    def clean(self):
        try:
            sc = UsoFactura.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk!=sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except UsoFactura.DoesNotExist:
            pass
        return self.cleaned_data

class ComprasEncForm(forms.ModelForm):
    fecha_compra = forms.DateInput()
    """fecha_factura = forms.DateInput()"""
    class Meta:
        model=ComprasEnc
        fields=['proveedor','empresaoc','fecha_compra','observacion',
            'no_factura','sub_total',
            'descuento','descuento2','total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['proveedor'].widget.attrs['class'] = 'form-control select2'
        self.fields['fecha_compra'].widget.attrs['readonly'] = True
        """self.fields['fecha_factura'].widget.attrs['readonly'] = True"""
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        """self.fields['descuento2'].widget.attrs['readonly'] = True"""
        self.fields['total'].widget.attrs['readonly'] = True