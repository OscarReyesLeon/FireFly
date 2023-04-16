from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
#from django_datatables_view.base_datatable_view import BaseDatatableView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.urls import reverse
from apps.core.urls import PREFIX_CREATE, PREFIX_UPDATE, PREFIX_DELETE
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from django.contrib import messages

class General(LoginRequiredMixin):
    def __init__(self, 
        prefix_app_url, prefix,form_class=None, prefix_text=None,
        femenine=False,
        text_form_create=None,
        model = None,
        *args, **kwargs):
        self.model = form_class.Meta.model if model is None else model
        self.form_class = form_class
        self.prefix = prefix
        self.prefix_app_url = prefix_app_url
        self.prefix_text = prefix_text if prefix_text is not None else prefix

        self.femenine = femenine
        if self.femenine:
            self.text_form_type = 'Crear una nueva'
            self.text_delete_type = 'eliminada'
        else:
            self.text_form_type = 'Crear un nuevo'
            self.text_delete_type = 'eliminado'
        self.text_form_create = '{} {}'.format(self.text_form_type, self.prefix_text) if text_form_create is None else text_form_create

    def get_queryset(self):
        return self.model.objects.all()
class GenericListMixin(General):
    def __init__(self,current_serializer,fields_full_text_search=[], 
                exclude_fields_full_text_search=[], order_complex_fields=None,
                template_list=None,table_title_complete=None,table_title=None,
                *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_list = 'layouts/partial/list_base.html' if template_list is None else template_list
        self.name_file_list_js = 'js/{}/{}_list.js'.format(self.prefix_app_url,self.prefix)
        if table_title_complete is None:
            self.table_title = 'Listado de {}s'.format(self.prefix_text) if table_title is None else table_title
        else:
            self.table_title = 'Listado de {}'.format(table_title_complete)

        #API
        self.current_serializer = current_serializer
        self.fields_full_text_search = fields_full_text_search
        self.exclude_fields_full_text_search = exclude_fields_full_text_search
        self.order_complex_fields = order_complex_fields

        self.url_create = '{}:{}_{}'.format(self.prefix_app_url, self.prefix, PREFIX_CREATE)
        self.url_update = '{}:{}_{}'.format(self.prefix_app_url, self.prefix, PREFIX_UPDATE)
        self.url_delete = '{}:{}_{}'.format(self.prefix_app_url, self.prefix, PREFIX_DELETE)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data.update({
            'c_table_title': self.table_title,
            'c_url_create': self.url_create,
            'c_url_update': self.url_update,
            'c_url_delete': self.url_delete,
            "c_name_file_list_js": self.name_file_list_js,
            "c_text_button_create_list": self.text_form_create,
        })
        return data
    
class GenericFormMixin(General): 
    def __init__(self, template_form=None, form_with_address=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not hasattr(self, 'view_type'):
            self.view_type = None
        self.template_form = 'layouts/partial/form_base.html' if template_form is None else template_form
        self.form_with_address = form_with_address
        self.url_list = '{}:{}_list'.format(self.prefix_app_url, self.prefix)
        self.success_url = reverse(self.url_list)
        self.delete_message = 'Registro eliminado correctamente'

    def get_title_form_update(self, button_text):
        return f'{button_text}: {self.get_object()}'
    
    def form_valid(self, form):
            data = super().form_valid(form)
            capitalize = self.prefix_text.capitalize()
            if self.view_type == 'update':
                gender = 'actualizada' if self.femenine else 'actualizado'
            else:
                gender = 'creada' if self.femenine else 'creado'
            messages.success(self.request, 
                f'¡{capitalize} {gender} correctamente!'
            )
            return data

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
       
        self.success_url = reverse(self.url_list)
        print(self.view_type)
        if self.view_type == 'update':
            text_button = "Actualizar {}".format(self.prefix_text)
            title_form = self.get_title_form_update(text_button)
            
        else:
            title_form = self.text_form_create
            text_button = "Guardar {}".format(self.prefix_text)

        data.update({
            'c_url_list': self.url_list,
            'c_text_button': text_button,
            'c_title_form': title_form,
            'form_with_address': self.form_with_address,
            
        })
        return data
class ListViewAjaxMixin:
    def filter_queryset(self, qs):
        search = self.request.GET.get('search', None)
        from django.db.models import Q
        from functools import reduce
        if search:
            create_string = lambda x: Q(**{f'{x}__icontains': search})
            qs = qs.filter(reduce(lambda x, y: x | y,
                    map(create_string, self.fields_full_text_search)))
        order_column = self.request.GET.get('order_column', None)
        order_dir = self.request.GET.get('order_dir', None)
        if order_column and order_dir:
            if self.order_complex_fields:
                order_column = self.order_complex_fields.get(order_column, None)
                if order_column:
                    list_order = []
                    for column in order_column:
                        prefix = '-' if order_dir == 'desc' else ''
                        list_order.append(f'{prefix}{column}')
                    qs = qs.order_by(*list_order)
            else:
                prefix = '-' if order_dir == 'desc' else ''
                qs = qs.order_by(f'{prefix}{order_column}')
        return qs
    
    def get_pagination(self, qs):
        paginator = LimitOffsetPagination()
        paginator.default_limit = 100
        paginator.max_limit = 100
        self.request._mutable = True
        self.request.query_params = self.request.GET
        paginator.limit_query_param = 'length'
        paginator.offset_query_param = 'start'
        result_page = paginator.paginate_queryset(qs, self.request)
        return result_page
    
    def get_with_ajax(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:
            records_total = queryset.count()
            queryset = self.filter_queryset(queryset)
            records_filtered = queryset.count()
            result_page = self.get_pagination(queryset)
            data = self.current_serializer(result_page, many=True).data
        else:
            records_total = records_filtered = 0
            data = []
        return {
            'data': data,
            'recordsTotal': records_total,
            'recordsFiltered': records_filtered,
        }
class ListViewMixin(GenericListMixin, ListViewAjaxMixin, ListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = self.template_list
        self.view_type = 'list'

    def get_queryset(self, *args, **kwargs):
        if self.request.is_ajax():
            return super().get_queryset(*args, **kwargs)
        return self.model.objects.none()
    
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse(self.get_with_ajax(request, *args, **kwargs))
        return super().get(request, *args, **kwargs)

class CreateViewMixin(GenericFormMixin, CreateView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = self.template_form
        self.view_type = 'create'

    
class UpdateViewMixin(GenericFormMixin, UpdateView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = self.template_form
        self.view_type = 'update'

class DeleteViewMixin(GenericFormMixin, DeleteView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.view_type = 'delete'

    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            self.object.delete()
            return JsonResponse({'msg': self.delete_message})
        except Exception as e:
            return JsonResponse({'msg': str(e)}, status=400)