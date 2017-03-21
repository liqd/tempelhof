# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.home.blocks
import apps.projects.blocks
import django.db.models.deletion
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('events_list', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('count', wagtail.wagtailcore.blocks.IntegerBlock(help_text='How many events should be shown?', min_value=2))), icon='date')), ('text', wagtail.wagtailcore.blocks.RichTextBlock(icon='doc-full', template='home/blocks/text.html')), ('teasers', wagtail.wagtailcore.blocks.StructBlock((('teasers', wagtail.wagtailcore.blocks.ListBlock(apps.home.blocks.TeaserBlock)),))), ('columns', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ListBlock(apps.home.blocks.ColumnBlock)),))), ('projects', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('projects', wagtail.wagtailcore.blocks.ListBlock(apps.projects.blocks.CurrentProjectBlock))))))),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(related_name='+', blank=True, to='images.CustomImage', null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
