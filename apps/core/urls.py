from django.urls import path
PREFIX_LIST = 'list'
PREFIX_CREATE = 'create'
PREFIX_UPDATE = 'update'
PREFIX_DELETE = 'delete'
PREFIX_LOAD_DATA = 'loaddata'
PREFIXES_PK = {
    PREFIX_LIST: '',
    PREFIX_CREATE: PREFIX_CREATE,
    PREFIX_UPDATE: F'{PREFIX_UPDATE}/<int:pk>/',
    PREFIX_DELETE: F'{PREFIX_DELETE}/<int:pk>/',

    PREFIX_LOAD_DATA: F'load_data/',
}

PREFIXES_UUID = {
    PREFIX_LIST: '',
    PREFIX_CREATE: PREFIX_CREATE,
    PREFIX_UPDATE: F'{PREFIX_UPDATE}/<uuid:pk>/',
    PREFIX_DELETE: F'{PREFIX_DELETE}/<uuid:pk>/',

    PREFIX_LOAD_DATA: F'load_data/',
}

def get_urls_by_view(list_views, with_uuid=False):
    PREFIX_PK = PREFIXES_UUID if with_uuid else PREFIXES_PK
    urlpatterns = [
        path(f'{"" if getattr(view, "PREFIX_EMPTY", None) else view.PREFIX_URL + "/" }{PREFIX_PK[key]}', getattr(view, name, None).as_view(),
             name=f'{view.PREFIX_URL}_{key}')
        for view in list_views
        for name in dir(view)
        for key in PREFIX_PK.keys()
        if name.endswith('View') and key in name.lower()
    ]

    # for view in list_views:
    #     for name in dir(view):
    #         for key in PREFIX_PK.keys():
    #             print(key)
    #             # if name.endswith('View') and key in name.lower():
    #             #     view_name = f'{view.PREFIX_URL}_{key}'
    #             #     print(view_name)
    return urlpatterns