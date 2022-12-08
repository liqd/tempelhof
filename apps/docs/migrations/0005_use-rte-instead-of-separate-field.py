# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.fields
import wagtail.images.blocks
import wagtail.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docspage',
            name='body',
            field=wagtail.fields.StreamField((('documents_list', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock()), ('images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('body', wagtail.blocks.RichTextBlock(required=False))))),)),
        ),
    ]
