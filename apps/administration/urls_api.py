from django.urls import path
from apps.administration.api.options import AdministarationInitialAPIView
urlpatterns = [
    path('options/', AdministarationInitialAPIView.as_view(), name='options_api'),
]