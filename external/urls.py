#urls
from django.urls import path
from .views import report_sensor, report_remplazo, report_crudo
urlpatterns = [
    path('report_sensor/', report_sensor, name='report_sensor'),
    path('report_remplazo/', report_remplazo, name='report_remplazo'),
    path('report_crudo/', report_crudo, name='report_crudo'),
]