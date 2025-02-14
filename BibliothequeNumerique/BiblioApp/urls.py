"""
URL configuration for BibliothequeNumerique project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from BiblioApp.views import LoginView, DashboardPersonnelView, ajouter_livre, profile_view


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', LoginView.as_view()), name='profile'
    path('', LoginView.as_view(), name='login2'),
    path('', DashboardPersonnelView.as_view(), name='dashboardPersonnel'), 
    # path('', ProfileView.as_view()),
    # path('', profile_view, name='profile'),
    path('', profile_view, name='profile'),
    path('', ajouter_livre, name='ajouter_livre'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]

