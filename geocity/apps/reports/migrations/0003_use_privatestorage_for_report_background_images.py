# Generated by Django 3.2.13 on 2022-06-26 08:33

import django.core.validators
from django.db import migrations

from geocity.apps.accounts.fields import AdministrativeEntityFileField
from geocity.fields import PrivateFileSystemStorage


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0002_create_reports"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reportlayout",
            name="background",
            field=AdministrativeEntityFileField(
                blank=True,
                null=True,
                storage=PrivateFileSystemStorage(),
                upload_to="report_layout_backgrounds",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["png"]
                    )
                ],
                verbose_name='Image d\'arrière plan ("papier à en-tête")',
            ),
        ),
    ]
