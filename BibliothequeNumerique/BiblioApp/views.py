from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import (
    Emprunt, Personne, Etudiant, Auteur, Livre,
    Etranger, Abonnement, Emplacement, Etagere,
    Compartiment, Universite, Campus, Faculte,
    Departement, Classe
)
from .serializers import (
    EmpruntSerializer, PersonneSerializer, EtudiantSerializer, 
    AuteurSerializer, LivreSerializer, EtrangerSerializer,
    AbonnementSerializer, EmplacementSerializer, EtagereSerializer,
    CompartimentSerializer, UniversiteSerializer, CampusSerializer,
    FaculteSerializer, DepartementSerializer, ClasseSerializer
)

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer

class PersonneViewSet(viewsets.ModelViewSet):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer

class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer

class EtrangerViewSet(viewsets.ModelViewSet):
    queryset = Etranger.objects.all()
    serializer_class = EtrangerSerializer

class AbonnementViewSet(viewsets.ModelViewSet):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer

class EmplacementViewSet(viewsets.ModelViewSet):
    queryset = Emplacement.objects.all()
    serializer_class = EmplacementSerializer

class EtagereViewSet(viewsets.ModelViewSet):
    queryset = Etagere.objects.all()
    serializer_class = EtagereSerializer

class CompartimentViewSet(viewsets.ModelViewSet):
    queryset = Compartiment.objects.all()
    serializer_class = CompartimentSerializer

class UniversiteViewSet(viewsets.ModelViewSet):
    queryset = Universite.objects.all()
    serializer_class = UniversiteSerializer

class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer

class FaculteViewSet(viewsets.ModelViewSet):
    queryset = Faculte.objects.all()
    serializer_class = FaculteSerializer

class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
