# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivePage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='wagtailcore.Page', parent_link=True, serialize=False)),
                ('body', wagtail.wagtailcore.fields.StreamField((('archive_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('time', wagtail.wagtailcore.blocks.CharBlock()), ('link', wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.URLBlock()), ('label', wagtail.wagtailcore.blocks.CharBlock())))), ('documents', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtaildocs.blocks.DocumentChooserBlock())))))),))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
