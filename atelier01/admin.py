from django.contrib import admin

from .models import Atelier01
from .models import Participant
from .models import ValeurMetier
from .models import BienSupport
from .models import Evenement_redoute

admin.site.register(Atelier01)
admin.site.register(Participant)
admin.site.register(ValeurMetier)
admin.site.register(BienSupport)
admin.site.register(Evenement_redoute)