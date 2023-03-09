from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.urls import reverse
from apps.core.urls import PREFIX_CREATE, PREFIX_UPDATE, PREFIX_DELETE


class GenericMixin(LoginRequiredMixin):
    def __init__(
            self, form_class,
            prefix_app_url,prefix, prefix_text=None, 
            model=None, femenine=False,
            template_form=None,template_list=None, table_title=None, table_title_complete=None,
            delete_message=None, delete_text=None,
            text_button_create=None, text_form_create=None,
            text_button_update=None, text_form_update=None,
            **kwargs
            ):
        self.tipo_vista = None
        self.model = model if model is not None else form_class.Meta.model
        self.form_class = form_class
        self.template_list = '{}_list.html'.format(prefix) if template_list is None else template_list
        self.template_form = 'layouts/partial/form_base.html' if template_form is None else template_form
        self.prefix = prefix
        self.prefix_text = prefix_text if prefix_text is not None else prefix
        self.url_list = '{}:{}_list'.format(prefix_app_url, prefix)
        self.success_url = reverse(self.url_list)
        self.url_create = '{}:{}_{}'.format(prefix_app_url, prefix, PREFIX_CREATE)
        self.url_update = '{}:{}_{}'.format(prefix_app_url, prefix, PREFIX_UPDATE)
        self.url_delete = '{}:{}_{}'.format(prefix_app_url, prefix, PREFIX_DELETE)
        if table_title_complete is None:
            self.table_title = 'Listado de {}s'.format(self.prefix_text) if table_title is None else table_title
        else:
            self.table_title = 'Listado de {}'.format(table_title_complete)
        
        self.femenine = femenine
        if self.femenine:
            text_form_type = 'Crear una nueva'
            text_delete_type = 'eliminada'
        else:
            text_form_type = 'Crear un nuevo'
            text_delete_type = 'eliminado'

        self.text_form_create = '{} {}'.format(text_form_type, self.prefix_text) if text_form_create is None else text_form_create
        self.text_button_create = 'Guardar {}'.format(self.prefix_text) if text_button_create is None else text_button_create
        self.text_button_update = 'Actualizar {}'.format(self.prefix_text) if text_button_update is None else text_button_update
        self.text_form_update = 'Actualizar {}'.format(self.prefix_text) if text_form_update is None else text_form_update
        self.delete_message = '{} {} exitosamente'.format(text_delete_type,self.prefix_text.capitalize()) if delete_message is None else delete_message
        self.delete_text = '¿Estas seguro de eliminar el registro {}'.format(self.get_complemento_delete_text() if delete_text is None else delete_text)

    def get_title_form_update(self):
        return f'{self.text_form_update}: {self.object}'
    
    def get_complemento_delete_text(self):
        return "{} {}".format('de la' if self.femenine else 'del', self.prefix_text)
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        #if funcion get_titulo_formulario en clase
        if self.tipo_vista == 'update':
            title_form = self.get_title_form_update()
            text_button = self.text_button_update
        else:
            title_form = self.text_form_create
            text_button = self.text_button_create

        data.update({
            'c_table_title': self.table_title,
            'c_title_form': title_form,
            'c_text_button': text_button,
            "c_text_button_create_list": self.text_form_create,
            'c_delete_text': self.delete_text,
            'c_url_list': self.url_list,
            'c_url_create': self.url_create,
            'c_url_update': self.url_update,
            'c_url_delete': self.url_delete,
        })
        return data

class ListViewMixin(GenericMixin, ListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = self.template_list
        self.tipo_vista = 'list'

class CreateViewMixin(GenericMixin, CreateView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = self.template_form
        self.tipo_vista = 'create'
    
class UpdateViewMixin(GenericMixin, UpdateView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = self.template_form
        self.tipo_vista = 'update'

class DeleteViewMixin(GenericMixin, DeleteView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo_vista = 'delete'

    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            self.object.delete()
            return JsonResponse({'msg': self.delete_message})
        except Exception as e:
            return JsonResponse({'msg': str(e)}, status=400)