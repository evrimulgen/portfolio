# Generated by Django 2.0.7 on 2018-07-23 19:13

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0020_add-verbose-name'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.CharField(max_length=255)),
                ('summary', wagtail.core.fields.RichTextField(help_text='Short description to show on tiles and lists')),
                ('description', wagtail.core.fields.RichTextField(help_text='Long description to show on the detail page')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, help_text='Duration in months, null=till now', null=True)),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
