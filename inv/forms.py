from django import forms

from .models import Banco, Computadora, Empleado, Equipo, Herramienta, Proceso, Categoria, Puesto, \
    UnidadMedida, Producto, Pedido, Autoriza, Computadora, Empresa, Genero, Estudios, Departamento, Nombresrelacion, Artciulosestandarizados

from cmp.models import ComprasEnc


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción de la Equipo",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ProcesoForm(forms.ModelForm):
    equipo = forms.ModelChoiceField(
        queryset=Equipo.objects.filter(estado=True)
            .order_by('descripcion')
    )

    class Meta:
        model = Proceso
        fields = ['equipo', 'descripcion', 'estado']
        labels = {'descripcion': "Proceso",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['equipo'].empty_label = "Seleccione Equipo"


class AutorizaForm(forms.ModelForm):
    class Meta:
        model = Autoriza
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción del Autorizante",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción de la Categoria",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UMForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción de la Categoria",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'codigo_barra', 'descripcion', 'estado', 'precio', 'existencia', 'ultima_compra', 'categoria', 'unidad_medida', 'foto']
        exclude = ['um', 'fm', 'uc', 'fc', 'proceso']
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cantidad', 'UniMed', 'proceso', 'autpor', 'comentario', 'precio_uni', 'articulo']
        """exclude = ['status', 'status2', 'fc', 'uc', 'fm', 'fecha_rechazo', indentificador_estado]"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['estandarizadoprodu'].widget.attrs['class'] = 'form-control select2'
        """self.fields['preciotransaccion'].widget.attrs['readonly'] = True"""
        """self.fields['um'].widget.attrs['readonly'] = True"""
        """self.fields['fecha_finalizado'].widget.attrs['readonly'] = True"""
        """self.fields['fecha_rechazo'].widget.attrs['readonly'] = True"""
class PedidoSecondForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cantidad', 'UniMed', 'articulo', 'proceso', 'autpor', 'comentario', 'precio_uni']
        """exclude = ['status', 'status2', 'fc', 'uc', 'fm', 'fecha_rechazo', indentificador_estado]"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
class PedidoComprasForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cantidad', 'UniMed', 'articulo', 'proceso', 'autpor', 'motivo_peticion', 'comentario', 'precio_uni', 'iva', 'divisa', 'preciotransaccion', 'folio_ingreso']
        """exclude = ['status', 'status2', 'fc', 'uc', 'fm', 'fecha_rechazo', indentificador_estado]"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['preciotransaccion'].widget.attrs['readonly'] = True
        self.fields['articulo'].widget.attrs['readonly'] = True
        self.fields['proceso'].widget.attrs['readonly'] = True
        self.fields['autpor'].widget.attrs['readonly'] = True

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['descripcion']
        labels = {'descripcion': "Descripción del Banco",}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class PuestoForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción del puesto",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        exclude = ['um', 'fm', 'uc', 'fc']
        labels = {'nombre': "Nombres"}
        widget = {'nombre': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ComputadoraForm(forms.ModelForm):
    class Meta:
        model = Computadora
        exclude = ['um', 'fm', 'uc', 'fc']
        labels = {'nombre': "descripción"}
        widget = {'nombre': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class HerramientaForm(forms.ModelForm):
    class Meta:
        model = Herramienta
        exclude = ['um', 'fm', 'uc', 'fc']
        labels = {'descripcion': "descripción"}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['descripcion', 'estado','razonsocial','rfcempresa','direccionfiscal','direccionentrega','urllogoempresa','horarios']
        labels = {'descripcion': "Descripción de la empresa",
            "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción del genero",
            "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class EstudiosForm(forms.ModelForm):
    class Meta:
        model = Estudios
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Nivel estudios",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class EcivilForm(forms.ModelForm):
    class Meta:
        model = Estudios
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Estado civil",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ParentescocontactoForm(forms.ModelForm):
    class Meta:
        model = Estudios
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Parentesco del familiar",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Departamento",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })



class ArtciulosestandarizadosForm(forms.ModelForm):
    class Meta:
        model = Artciulosestandarizados
        exclude = ['um', 'fm', 'uc', 'fc', 'estado', 'preciosugerido','precio2','precio3','precio4','fechapreciosugerido','fecha2','fecha3','fecha4']
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class NombresrelacionForm(forms.ModelForm):
    class Meta:
        model = Nombresrelacion
        exclude = ['um', 'fm', 'uc', 'fc', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['relacion'].widget.attrs['class'] = 'form-control select2'


class ComprasEncForm(forms.ModelForm):
    fecha_compra = forms.DateInput()
    fecha_factura = forms.DateInput()

    class Meta:
        model = ComprasEnc
        fields = ['proveedor', 'fecha_compra', 'observacion',
                  'no_factura', 'fecha_factura', 'sub_total',
                  'descuento', 'total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fecha_compra'].widget.attrs['readonly'] = True
        self.fields['fecha_factura'].widget.attrs['readonly'] = True
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True
