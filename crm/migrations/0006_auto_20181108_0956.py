# Generated by Django 2.0.9 on 2018-11-08 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20181107_2310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name_plural': 'people'},
        ),
        migrations.AlterField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='crm.Employee'),
        ),
    ]
