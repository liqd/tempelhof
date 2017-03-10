# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('projects', '0001_add-project-page'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, serialize=False, to='wagtailcore.Page', parent_link=True, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
