# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_description-to-richtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='contact',
            field=models.EmailField(max_length=254, default='undefined@example.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventpage',
            name='place',
            field=models.CharField(max_length=32, default='undefined'),
            preserve_default=False,
        ),
    ]
