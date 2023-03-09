from django.contrib.auth import password_validation
from django.contrib.auth.models import User, Group, Permission
from django import forms
from apps.core.forms import GeneralForm

class UserForm(GeneralForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['groups'].widget.attrs.update({'col_default': 12})
        self.fields['user_permissions'].widget.attrs.update({'col_default': 12})
        
        if self.instance.pk:
            #Password is not required when updating
            self.fields['password1'].required = False
            self.fields['password2'].required = False
            self.fields["password1"].label = "Contraseña (Dejar en blanco si no desea cambiarla)"
            self.fields["password2"].help_text ="Dejar en blanco ambos campos de contraseña si no desea cambiar la contraseña."

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=True, help_text=password_validation.password_validators_help_text_html)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput, required=True, help_text='Ingrese la misma contraseña que antes, para verificación.')

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name',
            'username', 'email',
            'groups', 'user_permissions',
            'password1', 'password2',
            'is_active', 'is_staff' 
        )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        queryset = User.objects.filter(username__iexact=username)
        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)
        if username and queryset.exists():
            raise forms.ValidationError('Ya existe un usuario con ese nombre de usuario', code="unique")
        else:
            return username
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Las contraseñas no coinciden",
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True, *args, **kwargs):
        user = super().save(commit=commit, *args, **kwargs)
        if self.cleaned_data.get("password1", False):
            user.set_password(self.cleaned_data.get("password1"))
        user.groups.set(self.cleaned_data['groups'])
        user.user_permissions.set(self.cleaned_data['user_permissions'])
        return user
    
class GroupForm(GeneralForm):
    class Meta:
        model = Group
        fields = ('name', 'permissions')

        labels = {
            'name': 'Nombre del grupo',
            'permissions': 'Permisos del grupo',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['permissions'].widget.attrs.update({'col_default': 12})
        self.fields['name'].widget.attrs.update({'col_default': 12})
        self.fields['permissions'].help_text = 'Seleccione los permisos que tendrá este grupo de usuarios'

    def clean_name(self, *args, **kwargs):
        value = self.cleaned_data.get('name')
        value = value.strip()
        if ' ' in value:
            raise forms.ValidationError('El nombre del grupo no puede contener espacios', code='invalid')
        return value


class PermissionForm(GeneralForm):
    class Meta:
        model = Permission
        fields = ('name', 'codename', 'content_type')

        labels = {
            'name': 'Nombre del permiso',
            'codename': 'Código del permiso (Así se identificará a nivel código)',
            'content_type': 'Módulo al que pertenece el permiso',
        }
    
    def clean_code(self, *args, **kwargs):
        value = self.cleaned_data.get('codename')
        value = value.strip()
        if ' ' in value:
            raise forms.ValidationError('El código del permiso no puede contener espacios', code='invalid')
        return value
