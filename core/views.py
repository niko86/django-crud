from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin 
from django.shortcuts import render
from django.urls import reverse_lazy

@login_required
def index(request):
    return render(request, 'core/index.html')

class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'core/registration/login.html'
    success_url = reverse_lazy('core:index')
    success_message = "You were successfully logged in"

class LogoutFormView(SuccessMessageMixin, LogoutView):
    success_url = reverse_lazy('core:index')
    success_message = "You were successfully logged out"