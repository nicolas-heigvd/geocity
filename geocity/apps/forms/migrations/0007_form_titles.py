# Generated by Django 3.2.15 on 2022-11-09 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0006_formfield_inlines_order"),
    ]

    operations = [
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
            name="proxycontacttype",
            options={
                "verbose_name": "1.5 Contact",
                "verbose_name_plural": "1.5 Contacts",
            },
        ),
    ]
