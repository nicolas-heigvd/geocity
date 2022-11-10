# Generated by Django 3.2.15 on 2022-11-07 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("accounts", "0004_makeproxymodels"),
        ("forms", "0003_migrate_permits_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProxyAdministrativeEntity",
            fields=[],
            options={
                "verbose_name": "1.1 Configuration de l'entité administrative (commune, organisation)",
                "verbose_name_plural": "1.1 Configuration des entités administratives (commune, organisation)",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("accounts.administrativeentity",),
        ),
        migrations.CreateModel(
            name="ContactType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (7, "Architecte/Ingénieur"),
                            (6, "Association"),
                            (0, "Autres"),
                            (8, "Direction des travaux"),
                            (3, "Entreprise"),
                            (4, "Maître d'ouvrage"),
                            (2, "Propriétaire"),
                            (1, "Requérant (si différent de l'auteur de la demande)"),
                            (5, "Sécurité"),
                        ],
                        default=0,
                        verbose_name="type de contact",
                    ),
                ),
                (
                    "is_mandatory",
                    models.BooleanField(default=True, verbose_name="obligatoire"),
                ),
                (
                    "form_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_types",
                        to="forms.formcategory",
                        verbose_name="type de demande",
                    ),
                ),
                (
                    "integrator",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="auth.group",
                        verbose_name="Groupe des administrateurs",
                    ),
                ),
            ],
            options={
                "unique_together": {("type", "form_category")},
            },
        ),
        migrations.CreateModel(
            name="ProxyContactType",
            fields=[],
            options={
                "verbose_name": "1.6 Configuration du contact",
                "verbose_name_plural": "1.6 Configuration des contacts",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("forms.contacttype",),
        ),
    ]
