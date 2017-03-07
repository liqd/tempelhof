# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import apps.home.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('events_list', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('count', wagtail.wagtailcore.blocks.IntegerBlock(help_text='How many events should be shown?', min_value=2))), icon='date')), ('text', wagtail.wagtailcore.blocks.RichTextBlock(template='home/blocks/text.html', icon='doc-full')), ('teasers', wagtail.wagtailcore.blocks.StructBlock((('teasers', wagtail.wagtailcore.blocks.ListBlock(apps.home.blocks.TeaserBlock)),))))),
        ),
    ]
