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
            # return redirect('dashboardPersonnel') 
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        messages.success(request, 'mot de passe ou nom de l''utilisateur incorrect')
        return render(request, self.template_name)

class LogoutView(TemplateView):
    template_name = 'login2.html'
    
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)
    
class DashboardPersonnelView(TemplateView):
    template_name = 'dashboardPersonnel.html'    # Assure-toi que ce fichier existe dans templates
    
    
# class ProfileView(TemplateView):
#     template_name = 'profile.html'  # Remplace par le chemin de ton template

def profile_view(request):
    # Logique pour récupérer les données de profil de l'utilisateur
    return render(request, 'accounts/profile.html')


def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Enregistrer l'objet Livre dans la base de données
            return redirect('nom_de_votre_vue_ou_page_de_confirmation')  # Rediriger après le succès
    else:
        form = LivreForm()  # Créer une instance vide du formulaire pour GET

    return render(request, 'ajouterLivre.html', {'form': form})

