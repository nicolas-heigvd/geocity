# Generated by Django 3.2.13 on 2022-06-09 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("permits", "0071_add_complementary_documents_inquiry_and_archived_requests"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="complementarydocumenttype",
            options={
                "verbose_name": "1.7 Configuration du type de document",
                "verbose_name_plural": "1.7 Configuration des types de document",
            },
        ),
        migrations.AddField(
            model_name="complementarydocumenttype",
            name="integrator",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="auth.group",
                verbose_name="Groupe des administrateurs",
            ),
        ),
    ]
