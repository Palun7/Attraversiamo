from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UpdateUsernameForm, CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash



class Login(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('core:index')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('usuarios:login')
    template_name = 'usuarios/signup.html'

@login_required
def update_username(request):
    if request.method == 'POST':
        form = UpdateUsernameForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu nombre de usuario se cambió con éxito.')
            return redirect('core:index')
    else:
        form = UpdateUsernameForm(instance=request.user)
    return render(request, 'login/update_username.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña se actualizó con éxito.')
            return redirect('core:index')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'login/change_password.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')