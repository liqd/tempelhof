# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import apps.home.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_add-teaser-block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField((('events_list', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('count', wagtail.core.blocks.IntegerBlock(min_value=2, help_text='How many events should be shown?'))), icon='date')), ('text', wagtail.core.blocks.RichTextBlock(icon='doc-full', template='home/blocks/text.html')), ('teasers', wagtail.core.blocks.StructBlock((('teasers', wagtail.core.blocks.ListBlock(apps.home.blocks.TeaserBlock)),))), ('columns', wagtail.core.blocks.StructBlock((('columns', wagtail.core.blocks.ListBlock(apps.home.blocks.ColumnBlock)),))))),
        ),
    ]
