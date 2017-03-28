# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtaildocs.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('images', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocsPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='wagtailcore.Page', primary_key=True)),
                ('body', wagtail.wagtailcore.fields.StreamField((('documents_list', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('documents', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtaildocs.blocks.DocumentChooserBlock()))))),))),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
