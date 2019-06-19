# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.images.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docspage',
            name='body',
            field=wagtail.core.fields.StreamField((('documents_list', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock()), ('images', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('documents', wagtail.core.blocks.ListBlock(wagtail.documents.blocks.DocumentChooserBlock()))))),)),
        ),
    ]
