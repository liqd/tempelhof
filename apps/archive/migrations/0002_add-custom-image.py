# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_add-archive'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivepage',
            options={'verbose_name': 'Archive'},
        ),
        migrations.AlterField(
            model_name='archivepage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True, related_name='+', to='images.CustomImage'),
        ),
    ]
