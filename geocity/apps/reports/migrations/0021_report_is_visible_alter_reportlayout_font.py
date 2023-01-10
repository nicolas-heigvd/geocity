# Generated by Django 4.1.4 on 2023-01-10 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0020_merge_20230110_0919"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="is_visible",
            field=models.BooleanField(
                default=True,
<<<<<<< HEAD
                help_text="Rendre le modèle visible dans la liste des documents et impressions (décocher pour les modèles de confirmation / remboursement de paiement)",
=======
                help_text="Cocher si le modèle doit être visible dans la liste des documents et impressions",
>>>>>>> fb3f9f03 (remove unused code. Add to model a way to hide/show models of documents (YC-1013))
                verbose_name="Visible",
            ),
        ),
        migrations.AlterField(
            model_name="reportlayout",
            name="font",
            field=models.CharField(
                blank=True,
                help_text='La liste des polices disponibles est visible sur <a href="https://fonts.google.com/" target="_blank">Google Fonts</a>',
                max_length=1024,
                null=True,
                verbose_name="Police",
            ),
        ),
    ]
