# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_add_calendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='description',
            field=wagtail.core.fields.RichTextField(max_length=512),
        ),
    ]
