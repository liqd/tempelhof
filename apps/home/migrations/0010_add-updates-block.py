# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.home.blocks
import wagtail.core.blocks
import apps.projects.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_add-custom-image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField((('text', wagtail.core.blocks.RichTextBlock(icon='doc-full', template='home/blocks/text.html')), ('teasers', wagtail.core.blocks.StructBlock((('teasers', wagtail.core.blocks.ListBlock(apps.home.blocks.TeaserBlock)),))), ('columns', wagtail.core.blocks.StructBlock((('columns', wagtail.core.blocks.ListBlock(apps.home.blocks.ColumnBlock)),))), ('projects', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock()), ('projects', wagtail.core.blocks.ListBlock(apps.projects.blocks.CurrentProjectBlock))))), ('updates', wagtail.core.blocks.StructBlock((('status', wagtail.core.blocks.PageChooserBlock(target_model='blog.BlogEntryPage')), ('calendar', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)),)))))))),
        ),
    ]
