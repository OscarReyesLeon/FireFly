#urls
from django.urls import path
from .views import report_sensor
urlpatterns = [
    path('report_sensor/', report_sensor, name='report_sensor'),
]