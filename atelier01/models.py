from django.db import models
from etude.models import Participant
# Create your models here.
class Atelier01 (models.Model):
    nom_societe = models.CharField(default="societe", max_length=30)
    description = models.TextField()
    particiant = models.ManyToManyField(
        Participant,
        verbose_name=("Participants"),
        related_name="ro_to_couples",
        blank=True,
        on_delete=models.CASCADE,
    )###
"""     created_at = models.DateTimeField(auto_now_add=True, default = timezone.now)
 """    #role = models.ManyToOneRel




class ValeurMetier(models.Model):
    nom = models.CharField(max_length=30)
    mission = models.CharField(max_length=200)
    description = models.TextField(null = True)
    responsabe = models.ForeignKey(
        Participant,
        verbose_name= "Entité responsable",
        on_delete=models.CASCADE,
        null=True 
    )

    class TypeVM(models.TextChoices):
        PROCESSUS = "processus"
        INFORMATION = "information"

    nature_vm = models.TextField(
         verbose_name=("nature "),
         choices = TypeVM.choices,
         default= TypeVM.INFORMATION
    )


class BienSupport(models.Model):
    nom_entite = models.TextField()
    vm_associe = models.TextField(
        verbose_name=("Valeur métier associé")
    ) #foreign key
    description = models.TextField(default = "description")
    responsable = models.TextField() #un des respnsables 
    #gotta change all short fields to charfield


class Evenement_redoute(models.Model):
    vm_associe = models.TextField(verbose_name=("Valeur métier associé")) #foreign key
    description = models.TextField(default = "description")
    
    class TypesImpact(models.TextChoices):
        SOCIAL = "social"
        SERVICE = "service"
        JURIDIQUE = "juridique"
        GOUVERNANCE = "gouvernance"
        FINANCIER = "financier"
        REPUTATION = "reputation"
        HUMAIN = "humain"
        MATERIEL = "materiel"

    impact = models.TextField(
        choices = TypesImpact.choices,
        default= TypesImpact.REPUTATION
    )

    class DegreGravite(models.IntegerChoices):
        MINEUR = 1, "mineur"
        SIGNIFICATIF = 2, "significatif"
        IMPORTANT = 3, "important"
        CRITIQUE = 4, "critique"

    gravite = models.PositiveSmallIntegerField(
        choices = DegreGravite.choices,
        default = DegreGravite.MINEUR
    )