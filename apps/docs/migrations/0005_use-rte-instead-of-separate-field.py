# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.core.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docspage',
            name='body',
            field=wagtail.core.fields.StreamField((('documents_list', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock()), ('images', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('body', wagtail.core.blocks.RichTextBlock(required=False))))),)),
        ),
    ]
