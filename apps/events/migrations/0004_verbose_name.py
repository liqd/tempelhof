# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170314_1035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calendarpage',
            options={'verbose_name': 'Calendar'},
        ),
        migrations.AlterModelOptions(
            name='eventpage',
            options={'verbose_name': 'Event'},
        ),
    ]
