# Generated by Django 2.0.9 on 2018-10-11 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_projectpage_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectpage',
            old_name='url',
            new_name='project_url',
        ),
    ]
