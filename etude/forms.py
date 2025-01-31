from django import forms
from .models import Etude

class EtudeForm(forms.ModelForm):
    class Meta:
        model = Etude
        fields = ['nom', 'description']
