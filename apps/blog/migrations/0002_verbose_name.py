# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_add-blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogentrypage',
            options={'verbose_name': 'Blog Entry'},
        ),
        migrations.AlterModelOptions(
            name='blogindexpage',
            options={'verbose_name': 'Blog'},
        ),
    ]
