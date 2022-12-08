# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.fields
import wagtail.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField((('events_list', wagtail.blocks.StructBlock((('heading', wagtail.blocks.CharBlock(required=False)), ('count', wagtail.blocks.IntegerBlock(help_text='How many events should be shown?', min_value=2))), icon='date')), ('text', wagtail.blocks.RichTextBlock())), default=''),
            preserve_default=False,
        ),
    ]
