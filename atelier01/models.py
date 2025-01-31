from django.db import models
from etude.models import Participant, Mission, Valeur_metier, Evenement_redoute, Socle_de_securite


class Atelier01 (models.Model):
    nom_societe = models.CharField(default="societe", max_length=30)
    description = models.TextField()
    #the participants belong to the first workshop
    participants = models.ManyToManyField(
        "etude.Participant",          # The related model
        #related_name="ateliers",      # Reverse lookup name for the relationship
        verbose_name="Participants",  # Label for the admin panel
        blank=True,                   # Allows the field to be optional
        symmetrical=False,            # Ensures the relationship isn't automatically reciprocal
        through="AtelierParticipant", # Custom intermediary table
    )
    mission = models.ManyToManyField(
        Mission,
        #related_name= "mission",
        verbose_name= "mission",
    )
    valeur_metier = models.ManyToManyField(
        Valeur_metier,
        #related_name= "valeurs metier",
        verbose_name= "valeur metier",
    )
    evenement_redoute = models.ManyToManyField(
        Evenement_redoute
    )
    socle_de_securite = models.ManyToManyField(
        Socle_de_securite,
        verbose_name= 'socle de sécurité'
    )
    #@property
    #def __str__(self):
    #    return self.nom_societe

#intermediate table for participants atelier01 relation
class AtelierParticipant(models.Model):
    atelier     = models.ForeignKey(Atelier01, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    date_joined = models.DateField()
