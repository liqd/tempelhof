# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('images', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntryPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='wagtailcore.Page')),
                ('text', wagtail.wagtailcore.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='wagtailcore.Page')),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
