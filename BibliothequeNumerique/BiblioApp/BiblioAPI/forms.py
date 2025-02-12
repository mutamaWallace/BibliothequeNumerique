from django import forms
from .models import (
    Emprunt, Personne, Etudiant, Auteur, Livre,
    Etranger, Abonnement, Emplacement, Etagere,
    Compartiment, Universite, Campus, Faculte,
    Departement, Classe
)

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['date_retour']

class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'email', 'password', 'genre', 'profil', 'tel', 'matricule', 'datenaissance', 'CNI', 'id_emprunt']

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email', 'password', 'genre', 'photo_passport', 'datenaissance', 'id_emprunt']

class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ['nom', 'prenom']

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'langueLivre', 'annee_publication', 'nombrepages', 'imageLivre', 'auteur', 'id_emplacement']

class EtrangerForm(forms.ModelForm):
    class Meta:
        model = Etranger
        fields = ['nom', 'prenom', 'email', 'password', 'genre', 'photo_passport', 'datenaissance', 'CNI', 'id_emprunt']

class AbonnementForm(forms.ModelForm):
    class Meta:
        model = Abonnement
        fields = ['type_abonnement', 'date_debut', 'date_fin']

class EmplacementForm(forms.ModelForm):
    class Meta:
        model = Emplacement
        fields = ['numero']

class EtagereForm(forms.ModelForm):
    class Meta:
        model = Etagere
        fields = ['nom', 'etat_etagere', 'mobilite', 'charge_maximal', 'id_emplacement']

class CompartimentForm(forms.ModelForm):
    class Meta:
        model = Compartiment
        fields = ['nom', 'nombreLivre', 'etagere']

class UniversiteForm(forms.ModelForm):
    class Meta:
        model = Universite
        fields = ['nom', 'pays', 'ville', 'email', 'site_web', 'id_campus']

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['campus', 'code']

class FaculteForm(forms.ModelForm):
    class Meta:
        model = Faculte
        fields = ['faculte', 'id_universite']

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['departement', 'id_faculte']

class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ['niveau', 'id_departement']