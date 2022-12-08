# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.home.blocks
import apps.projects.blocks
import django.db.models.deletion
import wagtail.fields
import wagtail.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField((('events_list', wagtail.blocks.StructBlock((('heading', wagtail.blocks.CharBlock(required=False)), ('count', wagtail.blocks.IntegerBlock(help_text='How many events should be shown?', min_value=2))), icon='date')), ('text', wagtail.blocks.RichTextBlock(icon='doc-full', template='home/blocks/text.html')), ('teasers', wagtail.blocks.StructBlock((('teasers', wagtail.blocks.ListBlock(apps.home.blocks.TeaserBlock)),))), ('columns', wagtail.blocks.StructBlock((('columns', wagtail.blocks.ListBlock(apps.home.blocks.ColumnBlock)),))), ('projects', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock()), ('projects', wagtail.blocks.ListBlock(apps.projects.blocks.CurrentProjectBlock))))))),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(related_name='+', blank=True, to='images.CustomImage', null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
