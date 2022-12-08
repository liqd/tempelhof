# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.blocks
import apps.home.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_add-teaser-block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField((('events_list', wagtail.blocks.StructBlock((('heading', wagtail.blocks.CharBlock(required=False)), ('count', wagtail.blocks.IntegerBlock(min_value=2, help_text='How many events should be shown?'))), icon='date')), ('text', wagtail.blocks.RichTextBlock(icon='doc-full', template='home/blocks/text.html')), ('teasers', wagtail.blocks.StructBlock((('teasers', wagtail.blocks.ListBlock(apps.home.blocks.TeaserBlock)),))), ('columns', wagtail.blocks.StructBlock((('columns', wagtail.blocks.ListBlock(apps.home.blocks.ColumnBlock)),))))),
        ),
    ]
