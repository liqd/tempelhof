# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields
import apps.home.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField((('events_list', wagtail.blocks.StructBlock((('heading', wagtail.blocks.CharBlock(required=False)), ('count', wagtail.blocks.IntegerBlock(help_text='How many events should be shown?', min_value=2))), icon='date')), ('text', wagtail.blocks.RichTextBlock(template='home/blocks/text.html', icon='doc-full')), ('teasers', wagtail.blocks.StructBlock((('teasers', wagtail.blocks.ListBlock(apps.home.blocks.TeaserBlock)),))))),
        ),
    ]
