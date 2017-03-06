# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('home', '0003_add_events_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', null=True, blank=True),
        ),
    ]
