# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_add-archive'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivepage',
            options={'verbose_name': 'Archive'},
        ),
    ]
