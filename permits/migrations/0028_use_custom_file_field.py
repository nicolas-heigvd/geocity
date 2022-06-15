# Generated by Django 3.2.4 on 2021-06-24 16:41

import django.core.validators
from django.db import migrations

import permits.fields


class Migration(migrations.Migration):

    dependencies = [
        ("permits", "0027_remove_usuned_fields_administrative_entity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worksobjecttype",
            name="directive",
            field=permits.fields.AdministrativeEntityFileField(
                blank=True,
                storage=permits.fields.PrivateFileSystemStorage(),
                upload_to="",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["pdf"]
                    )
                ],
                verbose_name="directive",
            ),
        ),
    ]
