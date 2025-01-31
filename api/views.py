from rest_framework.response import Response 
from rest_framework.decorators import api_view
from atelier01.models import AtelierParticipant,Atelier01 , Valeur_metier
from etude.models import Bien_support, Evenement_redoute #Socle_de_securite
from .serializers import Atelier01Serializer,AtelierParticipantSerializer,ValeurMetierSerializer,BienSupportSerializer,Evenement_redouteSerializer


@api_view(['GET'])
def getAtelierPart(request): 
    items = AtelierParticipant.objects.all()
    serializer = AtelierParticipantSerializer(items,many=True)
    print(Response(serializer.data))
    return Response(serializer.data)

@api_view(['GET'])
def getAtelier01(request): 
    items = Atelier01.objects.all()
    serializer = Atelier01Serializer(items,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getValeurMetier(request): 
    items = Valeur_metier.objects.all()
    serializer = ValeurMetierSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBienSupport(request): 
    items = Bien_support.objects.all()
    serializer = BienSupportSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEvenment(request): 
    items = Evenement_redoute.objects.all()
    serializer = Evenement_redouteSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['POST']) 
def addAtelierPart(request) :
    serializer = AtelierParticipantSerializer(data=request.data) 
    if serializer.is_valid() : 
        serializer.save()
    return Response(serializer.data)

@api_view(['POST']) 
def addAtelier01(request) :
    serializer = Atelier01Serializer(data=request.data) 
    if serializer.is_valid() : 
        serializer.save()
    return Response(serializer.data)

@api_view(['POST']) 
def addvaleurmetier(request) :
    serializer = ValeurMetierSerializer(data=request.data) 
    if serializer.is_valid() : 
        serializer.save()
    return Response(serializer.data)

@api_view(['POST']) 
def addBiensupport(request) :
    serializer = BienSupportSerializer(data=request.data) 
    if serializer.is_valid() : 
        serializer.save()
    return Response(serializer.data)

def addEvenment(request) :
    serializer = Evenement_redouteSerializer(data=request.data) 
    if serializer.is_valid() : 
        serializer.save()
    return Response(serializer.data)