# Generated by Django 3.2.15 on 2022-11-10 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0004_admin_reorder_for_phoenix"),
        ("accounts", "0003_migrate_permits_data"),
        ("forms", "0003_migrate_permits_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdministrativeEntityForAdminSite",
            fields=[],
            options={
                "verbose_name": "1.1 Entité administrative (commune, organisation)",
                "verbose_name_plural": "1.1 Entités administratives (commune, organisation)",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("accounts.administrativeentity",),
        ),
        migrations.CreateModel(
            name="ContactTypeForAdminSite",
            fields=[],
            options={
                "verbose_name": "1.5 Contact",
                "verbose_name_plural": "1.5 Contacts",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("submissions.contacttype",),
        ),
        migrations.AlterModelOptions(
            name="field",
            options={"verbose_name": "1.3 Champ", "verbose_name_plural": "1.3 Champs"},
        ),
        migrations.AlterModelOptions(
            name="form",
            options={
                "ordering": ("order",),
                "verbose_name": "1.4 Formulaire",
                "verbose_name_plural": "1.4 Formulaires",
            },
        ),
        migrations.AlterModelOptions(
            name="formcategory",
            options={
                "verbose_name": "1.2 Catégorie",
                "verbose_name_plural": "1.2 Catégories",
            },
        ),
        migrations.AlterModelOptions(
            name="formfield",
            options={
                "ordering": ("order",),
                "verbose_name": "Champ du formulaire",
                "verbose_name_plural": "Champs du formulaire",
            },
        ),
        migrations.AlterField(
            model_name="formfield",
            name="field",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="form_fields",
                to="forms.field",
                verbose_name="Champ",
            ),
        ),
        migrations.AlterField(
            model_name="formfield",
            name="order",
            field=models.PositiveSmallIntegerField(
                db_index=True, default=0, verbose_name="Position dans le formulaire"
            ),
        ),
    ]
