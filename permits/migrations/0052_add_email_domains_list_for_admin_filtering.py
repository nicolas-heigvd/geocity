# Generated by Django 3.2.7 on 2021-12-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("permits", "0051_remove_unused_print_model_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="permitdepartment",
            name="integrator_email_domains",
            field=models.CharField(
                blank=True,
                help_text="Liste de domaines séparés par des virgules ',' correspondant aux utilisateurs rattachés à l'entité administrative (ex: ma-commune.ch,commune.ch)",
                max_length=254,
                verbose_name="Domaines d'emails visibles pour l'intégrateur",
            ),
        ),
        migrations.AddField(
            model_name="permitdepartment",
            name="integrator_emails_exceptions",
            field=models.CharField(
                blank=True,
                help_text="Liste d'emails séparés par des virgules ',' d'utilisateurs spécifiques rattachés à l'entité administrative (ex: greffe@nowhere.com)",
                max_length=254,
                verbose_name="Emails complets visibles pour l'intégrateur",
            ),
        ),
    ]
