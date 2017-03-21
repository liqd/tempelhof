# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0002_add-images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docspage',
            options={'verbose_name': 'Documents'},
        ),
    ]
