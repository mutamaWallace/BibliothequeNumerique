from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EmpruntViewSet, PersonneViewSet, EtudiantViewSet,
    AuteurViewSet, LivreViewSet, EtrangerViewSet,
    AbonnementViewSet, EmplacementViewSet, EtagereViewSet,
    CompartimentViewSet, UniversiteViewSet, CampusViewSet,
    FaculteViewSet, DepartementViewSet, ClasseViewSet
)

router = DefaultRouter()
router.register(r'emprunts', EmpruntViewSet)
router.register(r'personnes', PersonneViewSet)
router.register(r'etudiants', EtudiantViewSet)
router.register(r'auteurs', AuteurViewSet)
router.register(r'lives', LivreViewSet)
router.register(r'etrangers', EtrangerViewSet)
router.register(r'abonnements', AbonnementViewSet)
router.register(r'emplacements', EmplacementViewSet)
router.register(r'etageres', EtagereViewSet)
router.register(r'compartiments', CompartimentViewSet)
router.register(r'universites', UniversiteViewSet)
router.register(r'campus', CampusViewSet)
router.register(r'facultes', FaculteViewSet)
router.register(r'departements', DepartementViewSet)
router.register(r'classes', ClasseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]