"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',include(('bases.urls','bases'), namespace='bases')),
    path('inv/',include(('inv.urls','inv'), namespace='inv')),
    path('cmp/', include(('cmp.urls', 'cmp'), namespace='cmp')),
    path('fac/', include(('fac.urls', 'fac'), namespace='fac')),
    path('bita/', include(('bita.urls', 'bita'), namespace='bita')),
    path('logi/', include(('logi.urls', 'logi'), namespace='logi')),
    path('external/', include(('apps.external.urls', 'external'), namespace='external')),
    path('administration/', include(('apps.administration.urls', 'administration'), namespace='administration')),
    path('auth/', include(('apps.users.urls', 'user'), namespace='user')),
    path('address/', include(('apps.address.urls', 'address'), namespace='address')),
    path('clients/', include(('apps.clients.urls', 'client'), namespace='client')),
    path('orders/', include(('apps.orders.urls', 'order'), namespace='order')),
    
    path('admin/', admin.site.urls),

    #PATH de API
    path('api/v1/administration/', include(('apps.administration.urls_api', 'api_administration'), namespace='api_administration')),
    path('api/v1/address/', include(('apps.address.urls_api', 'api_address'), namespace='api_address')),
    path('api/v1/clients/', include(('apps.clients.urls_api', 'api_client'), namespace='api_client')),
    path('api/v1/orders/', include(('apps.orders.urls_api', 'api_order'), namespace='api_order')),
    path('api/v1/users/', include(('apps.users.urls_api', 'api_user'), namespace='api_user')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'FireFly Manager'
