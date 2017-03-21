# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_add-project-index-page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectindexpage',
            options={'verbose_name': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='projectpage',
            options={'verbose_name': 'Project'},
        ),
    ]
