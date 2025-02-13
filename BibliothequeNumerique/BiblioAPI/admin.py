from django.contrib import admin
from BiblioAPI.models import *

# Register your models here.
@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_emprunt', 'date_retour')

@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'prenom', 'email', 'matricule')

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'prenom', 'email')

@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'prenom')

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'auteur', 'annee_publication')

@admin.register(Etranger)
class EtrangerAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'prenom', 'email')

@admin.register(Abonnement)
class AbonnementAdmin(admin.ModelAdmin):
    list_display = ('id','type_abonnement', 'date_debut', 'date_fin')

@admin.register(Emplacement)
class EmplacementAdmin(admin.ModelAdmin):
    list_display = ('id','numero',)

@admin.register(Etagere)
class EtagereAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'etat_etagere', 'mobilite')

@admin.register(Compartiment)
class CompartimentAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'nombreLivre')

@admin.register(Universite)
class UniversiteAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'pays', 'ville')

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('id','campus', 'code')

@admin.register(Faculte)
class FaculteAdmin(admin.ModelAdmin):
    list_display = ('id','faculte', 'id_universite')

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('id','departement', 'id_faculte')

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('id','niveau', 'id_departement')
