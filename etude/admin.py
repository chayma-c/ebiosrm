from django.contrib import admin
from .models import Etude, Socle_de_securite, Mission

admin.site.register(Etude)
admin.site.register(Socle_de_securite)
admin.site.register(Mission)