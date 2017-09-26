# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_rm-author-default'),
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('projects', '0005_add_detail_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectContainerPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='wagtailcore.Page')),
                ('short_description', models.CharField(max_length=112, help_text='Shown in list.')),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
                ('image', models.ForeignKey(blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='images.CustomImage')),
            ],
            options={
                'verbose_name': 'Projects',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='projectindexpage',
            options={'verbose_name': 'Project Containers'},
        ),
    ]
