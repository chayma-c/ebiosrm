from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _
from etude.models import Evenement_redoute


class RoTo(models.Model):
    class OrigineRisque(models.TextChoices):
        ETAT = "state", _("État")
        CRIME_ORGANISE = "organized_crime", _("Crime organisé")
        TERRORISTE = "terrorist", _("Terroriste")
        ACTIVISTE = "activist", _("Activiste")
        CONCURRENT = "competitor", _("Concurrence")
        AMATEUR = "amateur", _("Amateur")
        VENGEUR = "avenger", _("Vengeur")
        PATHOLOGIQUE = "pathological", _("Pathologique")

    class Motivation(models.IntegerChoices):
        NON_DEFINIE = 0, "non_définie"
        TRES_FAIBLE = 1, "très_faible"
        FAIBLE = 2, "faible"
        SIGNIFICATIVE = 3, "significative"
        FORTE = 4, "forte"

    class Ressources(models.IntegerChoices):
        NON_DEFINIE = 0, "non_définie"
        LIMITEES = 1, "limitées"
        SIGNIFICATIVES = 2, "significatives"
        IMPORTANTES = 3, "importantes"
        ILLIMITEES = 4, "illimitées"

    class Activite(models.IntegerChoices):
        NON_DEFINIE = 0, "non_définie"
        TRES_FAIBLE = 1, "très_faible"
        FAIBLE = 2, "faible"
        MODEREE = 3, "modérée"
        IMPORTANTE = 4, "importante"

    class Pertinence(models.IntegerChoices):
        NON_DEFINIE = 0, "non_définie"
        NON_PERTINENT = 1, "non_pertinent"
        PARTIELLEMENT_PERTINENT = 2, "partiellement_pertinent"
        ASSEZ_PERTINENT = 3, "assez_pertinent"
        TRES_PERTINENT = 4, "très_pertinent"

    #etude_ebios_rm = models.ForeignKey(
    #    EbiosRMStudy,
    #    verbose_name=_("Étude EBIOS RM"),
    #    on_delete=models.CASCADE,
    #)
    evenements_redoutes = models.ManyToManyField(
        Evenement_redoute,
        verbose_name=_("Événements redoutés"),
        related_name="ro_to_couples",
        blank=True,
    )

    origine_risque = models.CharField(
        max_length=32, 
        verbose_name=_("Origine du risque"), 
        choices=OrigineRisque.choices
    )
    objectif_cible = models.TextField(verbose_name=_("Objectif cible"))
    motivation = models.PositiveSmallIntegerField(
        verbose_name=_("Motivation"),
        choices=Motivation.choices,
        default=Motivation.NON_DEFINIE,
    )
    ressources = models.PositiveSmallIntegerField(
        verbose_name=_("Ressources"),
        choices=Ressources.choices,
        default=Ressources.NON_DEFINIE,
    )
    activite = models.PositiveSmallIntegerField(
        verbose_name=_("Activité"),
        choices=Activite.choices,
        default=Activite.NON_DEFINIE,
        validators=[MaxValueValidator(4)],
    )
    '''est_selectionne = models.BooleanField(verbose_name=_("Est sélectionné"), default=False)
    justification = models.TextField(verbose_name=_("Justification"), blank=True)

    fields_to_check = ["objectif_cible", "origine_risque"]

    def __str__(self) -> str:
        return f"{self.get_origine_risque_display()} - {self.objectif_cible}"

    class Meta:
        verbose_name = _("Couple OR/OC")
        verbose_name_plural = _("Couples OR/OC")
        ordering = ["created_at"]

    def save(self, *args, **kwargs):
        self.folder = self.etude_ebios_rm.folder
        super().save(*args, **kwargs)

    @property
    def get_pertinence(self):
        MATRICE_PERTINENCE = [
            [1, 1, 2, 2],
            [1, 2, 3, 3],
            [2, 3, 3, 4],
            [2, 3, 4, 4],
        ]
        if self.motivation == 0 or self.ressources == 0:
            return self.Pertinence(self.Pertinence.NON_DEFINIE).label
        return self.Pertinence(
            MATRICE_PERTINENCE[self.motivation - 1][self.ressources - 1]
        ).label

    def get_gravite(self):
        gravite = -1
        for evenement_redoute in self.evenements_redoutes.all():
            if evenement_redoute.gravity > gravite and evenement_redoute.is_selected:
                gravite = evenement_redoute.gravity
        return gravite'''


class Atelier02(models.Model):
    #source de risques
    objectif = "Identifier les Sources de Risque (SR) et leurs Objectifs Visés (OV) en lien avecl'objet de l'étude"
    SROV = models.ForeignKey(
        RoTo,
        on_delete=models.CASCADE,
        null = True
        )
