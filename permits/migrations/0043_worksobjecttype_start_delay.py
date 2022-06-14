# Generated by Django 3.2.7 on 2021-10-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("permits", "0042_add_regex_to_worksobjectproperty"),
    ]

    operations = [
        migrations.AddField(
            model_name="worksobjecttype",
            name="start_delay",
            field=models.IntegerField(
                blank=True,
                help_text="saisissez un nombre entier, positif ou négatif.",
                null=True,
                verbose_name="délai de commencement",
            ),
        ),
    ]
