# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.documents.blocks
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('images', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, to='wagtailcore.Page', serialize=False, auto_created=True, primary_key=True, on_delete=models.CASCADE)),
                ('body', wagtail.core.fields.StreamField((('archive_list', wagtail.core.blocks.StructBlock((('archives', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.TextBlock()), ('time', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()), ('label', wagtail.core.blocks.CharBlock())))), ('documents', wagtail.core.blocks.ListBlock(wagtail.documents.blocks.DocumentChooserBlock())))))),))),))),
                ('description', models.CharField(max_length=200)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True, blank=True, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
