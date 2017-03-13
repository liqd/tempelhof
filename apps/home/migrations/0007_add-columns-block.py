# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import apps.home.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_add-teaser-block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('events_list', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('count', wagtail.wagtailcore.blocks.IntegerBlock(min_value=2, help_text='How many events should be shown?'))), icon='date')), ('text', wagtail.wagtailcore.blocks.RichTextBlock(icon='doc-full', template='home/blocks/text.html')), ('teasers', wagtail.wagtailcore.blocks.StructBlock((('teasers', wagtail.wagtailcore.blocks.ListBlock(apps.home.blocks.TeaserBlock)),))), ('columns', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ListBlock(apps.home.blocks.ColumnBlock)),))))),
        ),
    ]
