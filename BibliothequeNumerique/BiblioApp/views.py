from django .shortcuts import render, redirect
from BiblioApp import *  
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import messages
from .forms import *


def login(request):
    return render(request, "login2.html")
class LoginView(TemplateView):
    
    template_name = 'login2.html'
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username = username, password = password)
        if user is not None and user.is_active:
            login(request)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        messages.success(request, 'mot de passe ou nom de l''utilisateur incorrect')
        return render(request, self.template_name)

class LogoutView(TemplateView):
    template_name = 'login2.html'
    
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)

        