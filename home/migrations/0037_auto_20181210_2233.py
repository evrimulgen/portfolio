# Generated by Django 2.0.9 on 2018-12-10 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20181210_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='responsibilities',
            field=models.ManyToManyField(blank=True, related_name='projects', to='home.Responsibility'),
        ),
    ]
