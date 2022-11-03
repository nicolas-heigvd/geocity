# Generated by Django 3.2.15 on 2022-10-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="permitdepartment",
            name="shortname",
            field=models.CharField(
                blank=True,
                help_text="Nom affiché par défaut dans les différentes étapes du formulaire, ne s'affiche pas dans l'admin (max. 32 caractères)",
                max_length=32,
                verbose_name="nom court",
            ),
        ),
    ]
