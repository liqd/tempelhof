# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpage',
            name='link',
        ),
        migrations.AddField(
            model_name='projectpage',
            name='embed_code',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectpage',
            name='short_description',
            field=models.CharField(max_length=112, default='', help_text='Shown in list.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
    ]
