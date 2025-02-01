from rest_framework.generics import ListCreateAPIView
from atelier01.models import AtelierParticipant, Atelier01, Valeur_metier
from etude.models import Bien_support, Evenement_redoute
from .serializers import (
    Atelier01Serializer,
    AtelierParticipantSerializer,
    ValeurMetierSerializer,
    BienSupportSerializer,
    Evenement_redouteSerializer,
)

class AtelierParticipantListCreateView(ListCreateAPIView):
    queryset = AtelierParticipant.objects.all()
    serializer_class = AtelierParticipantSerializer

class Atelier01ListCreateView(ListCreateAPIView):
    queryset = Atelier01.objects.all()
    serializer_class = Atelier01Serializer

class ValeurMetierListCreateView(ListCreateAPIView):
    queryset = Valeur_metier.objects.all()
    serializer_class = ValeurMetierSerializer

class BienSupportListCreateView(ListCreateAPIView):
    queryset = Bien_support.objects.all()
    serializer_class = BienSupportSerializer

class EvenementRedouteListCreateView(ListCreateAPIView):
    queryset = Evenement_redoute.objects.all()
    serializer_class = Evenement_redouteSerializer
