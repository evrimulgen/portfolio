# Generated by Django 2.0.7 on 2018-07-27 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180727_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technologyinfo',
            name='tag',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='taggit.Tag'),
        ),
    ]
