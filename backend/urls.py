from django.http import HttpResponse
from django.urls import path
from backend.HU03_ChangePassword.controllers.auth.ChangePasswordController import ChangePasswordController

urlpatterns = [
    path('api/change-password', ChangePasswordController.as_view(), name='change-password'),
    path('', lambda request: HttpResponse("Bienvenido a la API ")),
    
]
