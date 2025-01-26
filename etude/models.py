from django.db import models

# Create your models here.
#class Etude (models.Model):
    #nom = 
class Participant(models.Model):
    nom = models.CharField(max_length=30)
    role = models.CharField(max_length=120)
"""     atelier = models.ForeignKey(
        Atelier01,
        verbose_name="atelier", # à changer
        on_delete=models.CASCADE,
        null=True 
    ) """