# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('images', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, to='wagtailcore.Page', primary_key=True, parent_link=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, to='wagtailcore.Page', primary_key=True, parent_link=True, serialize=False)),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('short_description', models.CharField(max_length=56, help_text='Shown on the homepage.')),
                ('description', models.CharField(max_length=512)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
