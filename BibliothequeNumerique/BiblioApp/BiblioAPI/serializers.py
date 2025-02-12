from rest_framework import serializers
from .models import (
    Emprunt, Personne, Etudiant, Auteur, Livre,
    Etranger, Abonnement, Emplacement, Etagere,
    Compartiment, Universite, Campus, Faculte,
    Departement, Classe
)

class EmpruntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprunt
        fields = ['date_retour']

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'email', 'password', 'genre', 'profil', 'tel', 'matricule', 'datenaissance', 'CNI', 'id_emprunt']

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email', 'password', 'genre', 'photo_passport', 'datenaissance', 'id_emprunt']

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = ['nom', 'prenom']

class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = ['titre', 'langueLivre', 'annee_publication', 'nombrepages', 'imageLivre', 'auteur', 'id_emplacement']

class EtrangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etranger
        fields = ['nom', 'prenom', 'email', 'password', 'genre', 'photo_passport', 'datenaissance', 'CNI', 'id_emprunt']

class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = ['type_abonnement', 'date_debut', 'date_fin']

class EmplacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emplacement
        fields = ['numero']

class EtagereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etagere
        fields = ['nom', 'etat_etagere', 'mobilite', 'charge_maximal', 'id_emplacement']

class CompartimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compartiment
        fields = ['nom', 'nombreLivre', 'etagere']

class UniversiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universite
        fields = ['nom', 'pays', 'ville', 'email', 'site_web', 'id_campus']

class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = ['campus', 'code']

class FaculteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculte
        fields = ['faculte', 'id_universite']

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ['departement', 'id_faculte']

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ['niveau', 'id_departement']