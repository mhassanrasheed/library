# Generated by Django 3.1.7 on 2021-03-29 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resources',
            old_name='publication_data',
            new_name='publication_date',
        ),
    ]
