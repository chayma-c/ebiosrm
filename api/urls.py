from django.urls import path
from .views import (
    AtelierParticipantListCreateView,
    Atelier01ListCreateView,
    ValeurMetierListCreateView,
    BienSupportListCreateView,
    EvenementRedouteListCreateView,
)

urlpatterns = [
    path('atelier_participant/', AtelierParticipantListCreateView.as_view(), name='atelier_participant'),
    path('atelier01/', Atelier01ListCreateView.as_view(), name='atelier01'),
    path('valeur_metier/', ValeurMetierListCreateView.as_view(), name='valeur_metier'),
    path('bien_support/', BienSupportListCreateView.as_view(), name='bien_support'),
    path('evenement_redoute/', EvenementRedouteListCreateView.as_view(), name='evenement_redoute'),
]
