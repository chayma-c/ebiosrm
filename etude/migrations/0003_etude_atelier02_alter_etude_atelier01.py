# Generated by Django 5.1.5 on 2025-01-29 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atelier01', '0003_atelier01_evenement_redoute_atelier01_mission_and_more'),
        ('etude', '0002_evenement_redoute_mission_socle_de_securite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='etude',
            name='atelier02',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='atelier01.atelier01', verbose_name='atelier 02: Sources de risques'),
        ),
        migrations.AlterField(
            model_name='etude',
            name='atelier01',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='atelier01.atelier01', verbose_name='atelier 01: Cadrage et socle de sécurité'),
        ),
    ]
