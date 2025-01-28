from django.contrib import admin
from .models import Atelier01, Evenement_redoute
from etude.models import Participant, Valeur_metier, Bien_support

admin.site.register(Atelier01)
admin.site.register(Participant)
admin.site.register(Valeur_metier)
admin.site.register(Bien_support)
admin.site.register(Evenement_redoute)