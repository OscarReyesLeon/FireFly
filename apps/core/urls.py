from django.urls import path
PREFIX_LIST = 'list'
PREFIX_CREATE = 'create'
PREFIX_UPDATE = 'update'
PREFIX_DELETE = 'delete'

PREFIXES = {
    'list': '',
    'create': PREFIX_CREATE,
    'update': F'{PREFIX_UPDATE}/<int:pk>/',
    'delete': F'{PREFIX_DELETE}/<int:pk>/',
}

def get_urls_by_view(list_views):
    urlpatterns = [
        path(f'{view.PREFIX_URL}/{PREFIXES[key]}', getattr(view, name, None).as_view(),
             name=f'{view.PREFIX_URL}_{key}')
        for view in list_views
        for name in dir(view)
        for key in PREFIXES.keys()
        if name.endswith('View') and key in name.lower()
    ]
    return urlpatterns