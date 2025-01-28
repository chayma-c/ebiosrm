from rest_framework import serializers 
from atelier01.models import AtelierParticipant,Atelier01 , Valeur_metier
from etude.models import Bien_support, Evenement_redoute #Socle_de_securite
class Atelier01Serializer (serializers.ModelSerializer) :
    class Meta : 
        model = Atelier01 
        fields = '__all__'
class AtelierParticipantSerializer (serializers.ModelSerializer) :
    class Meta : 
        model = AtelierParticipant 
        fields = '__all__'
class ValeurMetierSerializer (serializers.ModelSerializer) :
    class Meta : 
        model = Valeur_metier 
        fields = '__all__'
class BienSupportSerializer (serializers.ModelSerializer) :
    class Meta : 
        model = Bien_support 
        fields = '__all__'
class Evenement_redouteSerializer (serializers.ModelSerializer) :
    class Meta : 
        model = Evenement_redoute 
        fields = '__all__'
