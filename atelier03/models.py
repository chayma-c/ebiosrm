from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

class Partie_prenante(models.Model):
    class Categorie(models.TextChoices):
        CLIENT = "client", _("Client")
        PARTNER = "partner", _("Partner")
        FOURNISSEUR = "fourisseur", _("fourisseur")

    categorie = models.CharField(
        max_length=32, verbose_name=_("Categorie"), choices=Categorie.choices
    )
    current_dependency = models.PositiveSmallIntegerField(
        verbose_name=_("Current dependency"),
        default=0,
        validators=[MaxValueValidator(4)],
    )
    current_penetration = models.PositiveSmallIntegerField(
        verbose_name=_("Current penetration"),
        default=0,
        validators=[MaxValueValidator(4)],
    )
    current_maturity = models.PositiveSmallIntegerField(
        verbose_name=_("Current maturity"),
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(4)],
    )
    current_trust = models.PositiveSmallIntegerField(
        verbose_name=_("Current trust"),
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(4)],
    )
    is_selected = models.BooleanField(verbose_name=_("Is selected"), default=False)
    justification = models.TextField(verbose_name=_("Justification"), blank=True)

    #fields_to_check = ["entity", "category"]
    @staticmethod
    def _compute_criticality(
        dependency: int, penetration: int, maturity: int, trust: int
    ):
        if (maturity * trust) == 0:
            return 0
        return (dependency * penetration) / (maturity * trust)
    @property
    def current_criticality(self):
        return self._compute_criticality(
            self.current_dependency,
            self.current_penetration,
            self.current_maturity,
            self.current_trust,
        )


    
class Atelier03(models.Model):
    objectif = "Identifier les parties prenantes critiques de l'écosystème et construire des scénarios de risque de haut niveau (scénarios stratégiques)."
    partie_prenante = models.ForeignKey(
        Partie_prenante,
        on_delete=models.CASCADE,
        null = True
    )

