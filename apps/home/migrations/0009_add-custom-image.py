# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.home.blocks
import apps.projects.blocks
import django.db.models.deletion
import wagtail.core.fields
import wagtail.core.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField((('events_list', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('count', wagtail.core.blocks.IntegerBlock(help_text='How many events should be shown?', min_value=2))), icon='date')), ('text', wagtail.core.blocks.RichTextBlock(icon='doc-full', template='home/blocks/text.html')), ('teasers', wagtail.core.blocks.StructBlock((('teasers', wagtail.core.blocks.ListBlock(apps.home.blocks.TeaserBlock)),))), ('columns', wagtail.core.blocks.StructBlock((('columns', wagtail.core.blocks.ListBlock(apps.home.blocks.ColumnBlock)),))), ('projects', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock()), ('projects', wagtail.core.blocks.ListBlock(apps.projects.blocks.CurrentProjectBlock))))))),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(related_name='+', blank=True, to='images.CustomImage', null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
