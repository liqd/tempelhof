# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('documents_list', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('images', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock())), ('body', wagtail.wagtailcore.blocks.RichTextBlock(required=False))))),)),
        ),
    ]
