# Generated by Django 2.0.9 on 2018-11-15 18:22

import datetime
from django.db import migrations
from django.utils.timezone import utc
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0022_auto_20181115_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2018, 11, 15, 18, 22, 44, 501875, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
