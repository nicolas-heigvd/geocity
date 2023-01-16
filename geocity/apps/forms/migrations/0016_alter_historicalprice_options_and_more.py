# Generated by Django 4.1.4 on 2023-01-16 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("forms", "0015_merge_20230110_0919"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalprice",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical 1.7 Tarif",
                "verbose_name_plural": "historical 1.7 Tarifs",
            },
        ),
        migrations.AddField(
            model_name="historicalprice",
            name="integrator",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="auth.group",
                verbose_name="Groupe des administrateurs",
            ),
        ),
        migrations.AddField(
            model_name="price",
            name="integrator",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="auth.group",
                verbose_name="Groupe des administrateurs",
            ),
        ),
    ]
