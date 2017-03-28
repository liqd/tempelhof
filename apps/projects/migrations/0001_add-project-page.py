# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('images', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to='wagtailcore.Page')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.CharField(max_length=256)),
                ('link', models.URLField()),
                ('image', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
