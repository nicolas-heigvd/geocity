# Generated by Django 3.2.15 on 2022-11-16 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_migrate_permits_data"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="administrativeentity",
            options={
                "verbose_name": "1.1 Configuration de l'entité administrative (commune, organisation)",
                "verbose_name_plural": "1.1 Configuration des entités administratives (commune, organisation)",
            },
        ),
    ]
