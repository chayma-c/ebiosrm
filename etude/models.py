from django.db import models
#from atelier01.models import Atelier01
# avoid direct import to avoid circular import

class Etude (models.Model):
    nom         = models.CharField(max_length= 100)
    description = models.TextField()
    atelier01   = models.ForeignKey(
        "atelier01.Atelier01",
        verbose_name = "atelier 01: Cadrage et socle de sécurité",
        on_delete    = models.CASCADE,
        null         = True
    )
    #atelier02 = models.ForeignKey(Atelier02)
    #atelier03 = models.ForeignKey(Atelier03)


#----------------atelier01------------------------
class Mission(models.Model):
    mission = models.CharField(max_length=250)

class Participant(models.Model):
    nom = models.CharField(max_length=30)
    role = models.CharField(max_length=120)

class Bien_support(models.Model):
    nom_entite = models.CharField(max_length=100)
    description = models.TextField(default = "description")
    responsable = models.ForeignKey(
        Participant,
        on_delete    = models.CASCADE,
        null         = True
    )

class Valeur_metier(models.Model):
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
        PROCESSUS   = "processus"
        INFORMATION = "information"

    nature_vm = models.CharField(
        max_length   = 50,
        verbose_name = "nature ",
        choices      = TypeVM.choices
    )
    bien_support = models.ManyToManyField(
        Bien_support
    )

class Evenement_redoute(models.Model):
    vm_associe = models.TextField(verbose_name=("Valeur métier associé")) #foreign key
    description = models.TextField(default = "description")
    
    class TypesImpact(models.TextChoices):
        SOCIAL      = "social"
        SERVICE     = "service"
        JURIDIQUE   = "juridique"
        GOUVERNANCE = "gouvernance"
        FINANCIER   = "financier"
        REPUTATION  = "reputation"
        HUMAIN      = "humain"
        MATERIEL    = "materiel"

    impact = models.TextField(
        choices = TypesImpact.choices,
        default = TypesImpact.REPUTATION
    )

    class DegreGravite(models.IntegerChoices):
        MINEUR       = 1, "mineur"
        SIGNIFICATIF = 2, "significatif"
        IMPORTANT    = 3, "important"
        CRITIQUE     = 4, "critique"

    gravite = models.PositiveSmallIntegerField(
        choices = DegreGravite.choices,
        default = DegreGravite.MINEUR
    )

class Socle_de_securite(models.Model):
    class typeReferentiel(models.TextChoices):
        NORMATIF = "Référentiel normatif International"
        REPDP    = "Règlement européen sur la protection des données personnelles"
        RHIBP    = "Règles d'hygiène informatique et bonnes pratiques Française"
        RBPAG    = "Règles de bonnes pratiques d'audit et de gouvernance Anglo-Saxon"

    referentiel = models.CharField(max_length=200)

    type = models.CharField(
        max_length = 200,
        choices    = typeReferentiel.choices,
        default    = typeReferentiel.NORMATIF 
    )

    class EtatSocle(models.TextChoices):
        AAR = "appliquée avec restriction"
        ASR = "appliquée sans restriction"

    etat = models.CharField(
        max_length= 200,
        choices = EtatSocle.choices,
        default = EtatSocle.AAR
    )