# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_add-custom-image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customimage',
            name='author',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
