# Generated by Django 2.0.9 on 2018-11-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_auto_20181110_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='duration',
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
