# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='short_description',
            field=models.CharField(max_length=112, help_text='Shown on the homepage.'),
        ),
    ]
