# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtaildocs.blocks
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


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
                ('page_ptr', models.OneToOneField(parent_link=True, to='wagtailcore.Page', serialize=False, auto_created=True, primary_key=True)),
                ('body', wagtail.wagtailcore.fields.StreamField((('archive_list', wagtail.wagtailcore.blocks.StructBlock((('archives', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('time', wagtail.wagtailcore.blocks.CharBlock()), ('link', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.URLBlock()), ('label', wagtail.wagtailcore.blocks.CharBlock())))), ('documents', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtaildocs.blocks.DocumentChooserBlock())))))),))),))),
                ('description', models.CharField(max_length=200)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True, blank=True, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
