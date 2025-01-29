from django import forms
from .models import Partie_prenante

class PartiePrenanteForm(forms.ModelForm):
    class Meta:
        model = Partie_prenante
        fields = [
            'categorie', 
            'current_dependency', 
            'current_penetration',
            'current_maturity',
            'current_trust',
            'is_selected',
            'justification'
        ]