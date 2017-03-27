# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.home.blocks
import wagtail.wagtailcore.blocks
import apps.projects.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_add-custom-image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.RichTextBlock(icon='doc-full', template='home/blocks/text.html')), ('teasers', wagtail.wagtailcore.blocks.StructBlock((('teasers', wagtail.wagtailcore.blocks.ListBlock(apps.home.blocks.TeaserBlock)),))), ('columns', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ListBlock(apps.home.blocks.ColumnBlock)),))), ('projects', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('projects', wagtail.wagtailcore.blocks.ListBlock(apps.projects.blocks.CurrentProjectBlock))))), ('updates', wagtail.wagtailcore.blocks.StructBlock((('status', wagtail.wagtailcore.blocks.PageChooserBlock(target_model='blog.BlogEntryPage')), ('calendar', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)),)))))))),
        ),
    ]
