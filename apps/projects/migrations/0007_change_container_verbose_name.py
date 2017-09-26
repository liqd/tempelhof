# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_container'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectcontainerpage',
            options={'verbose_name': 'Project Container'},
        ),
    ]
