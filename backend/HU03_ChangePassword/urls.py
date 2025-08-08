from django.contrib import admin
from django.urls import path, include
from django.urls import path
from views import ChangePasswordView

urlpatterns = [
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('changepassword.urls')),  # Asegúrate que este exista
]
