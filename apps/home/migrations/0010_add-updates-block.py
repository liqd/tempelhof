# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.home.blocks
import wagtail.blocks
import apps.projects.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_add-custom-image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField((('text', wagtail.blocks.RichTextBlock(icon='doc-full', template='home/blocks/text.html')), ('teasers', wagtail.blocks.StructBlock((('teasers', wagtail.blocks.ListBlock(apps.home.blocks.TeaserBlock)),))), ('columns', wagtail.blocks.StructBlock((('columns', wagtail.blocks.ListBlock(apps.home.blocks.ColumnBlock)),))), ('projects', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock()), ('projects', wagtail.blocks.ListBlock(apps.projects.blocks.CurrentProjectBlock))))), ('updates', wagtail.blocks.StructBlock((('status', wagtail.blocks.PageChooserBlock(target_model='blog.BlogEntryPage')), ('calendar', wagtail.blocks.StructBlock((('heading', wagtail.blocks.CharBlock(required=False)),)))))))),
        ),
    ]
