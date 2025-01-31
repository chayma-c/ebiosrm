from django import forms
from .models import Atelier01, AtelierParticipant
from etude.models import Mission, Valeur_metier, Evenement_redoute, Socle_de_securite, Participant

class Atelier01Form(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(
        queryset=Participant.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Participants"
    )
    mission = forms.ModelMultipleChoiceField(
        queryset=Mission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Mission"
    )
    valeur_metier = forms.ModelMultipleChoiceField(
        queryset=Valeur_metier.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Valeur métier"
    )
    evenement_redoute = forms.ModelMultipleChoiceField(
        queryset=Evenement_redoute.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Événement redouté"
    )
    socle_de_securite = forms.ModelMultipleChoiceField(
        queryset=Socle_de_securite.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Socle de sécurité"
    )

    class Meta:
        model = Atelier01
        fields = ['nom_societe', 'description', 'participants', 'mission', 'valeur_metier', 'evenement_redoute', 'socle_de_securite']

class AtelierParticipantForm(forms.ModelForm):
    class Meta:
        model = AtelierParticipant
        fields = ['atelier', 'participant', 'date_joined']
