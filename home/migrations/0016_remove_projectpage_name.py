# Generated by Django 2.0.8 on 2018-10-08 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_technologiespage_title_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpage',
            name='name',
        ),
    ]
