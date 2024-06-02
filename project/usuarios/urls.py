from django.urls import path
from .views import SignUpView, Login, change_password, update_username, perfil
from django.contrib.auth.views import LogoutView


app_name = 'usuarios'

urlpatterns = [
    path('usuarios/login', Login.as_view(), name='login'),
    path('usuarios/signup', SignUpView.as_view(template_name='usuarios/signup.html'), name='signup'),
    path('usuarios/logout', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('usuarios/update_username', update_username, name='update_username'),
    path('usuarios/change_password', change_password, name='change_password'),
    path('usuarios/perfil', perfil, name='perfil'),
]

