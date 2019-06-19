# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import apps.home.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField((('events_list', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('count', wagtail.core.blocks.IntegerBlock(help_text='How many events should be shown?', min_value=2))), icon='date')), ('text', wagtail.core.blocks.RichTextBlock(template='home/blocks/text.html', icon='doc-full')), ('teasers', wagtail.core.blocks.StructBlock((('teasers', wagtail.core.blocks.ListBlock(apps.home.blocks.TeaserBlock)),))))),
        ),
    ]
