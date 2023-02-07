# Generated by Django 4.1.4 on 2023-02-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "reports",
            "0025_rename_padding_top_sectionmailing_padding_top_mailing_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="sectiondetail",
            name="show_form_name",
            field=models.BooleanField(
                default=True,
                help_text="Cocher cette option affiche le nom du formulaire (objet et type de demande)",
                verbose_name="Afficher le nom du formulaire",
            ),
        ),
        migrations.AddField(
            model_name="sectiondetail",
            name="style",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "champ: valeur"), (1, "champ    valeur")],
                default=0,
                help_text="Choisir le style d'affichage",
                verbose_name="Page",
            ),
        ),
    ]
