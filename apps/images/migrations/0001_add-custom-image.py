# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers
import wagtail.wagtailimages.models
import django.db.models.deletion
import wagtail.wagtailsearch.index
from django.conf import settings
import wagtail.wagtailcore.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('file', models.ImageField(verbose_name='file', width_field='width', upload_to=wagtail.wagtailimages.models.get_upload_to, height_field='height')),
                ('width', models.IntegerField(verbose_name='width', editable=False)),
                ('height', models.IntegerField(verbose_name='height', editable=False)),
                ('created_at', models.DateTimeField(verbose_name='created at', auto_now_add=True, db_index=True)),
                ('focal_point_x', models.PositiveIntegerField(null=True, blank=True)),
                ('focal_point_y', models.PositiveIntegerField(null=True, blank=True)),
                ('focal_point_width', models.PositiveIntegerField(null=True, blank=True)),
                ('focal_point_height', models.PositiveIntegerField(null=True, blank=True)),
                ('file_size', models.PositiveIntegerField(null=True, editable=False)),
                ('author', models.CharField(default='THF', max_length=128, blank=True)),
                ('collection', models.ForeignKey(default=wagtail.wagtailcore.models.get_root_collection_id, related_name='+', verbose_name='collection', to='wagtailcore.Collection')),
                ('tags', taggit.managers.TaggableManager(through='taggit.TaggedItem', blank=True, to='taggit.Tag', verbose_name='tags', help_text=None)),
                ('uploaded_by_user', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user', on_delete=django.db.models.deletion.SET_NULL, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.wagtailsearch.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='CustomRendition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('filter_spec', models.CharField(max_length=255, db_index=True)),
                ('file', models.ImageField(width_field='width', upload_to=wagtail.wagtailimages.models.get_rendition_upload_to, height_field='height')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('focal_point_key', models.CharField(default='', max_length=16, blank=True, editable=False)),
                ('image', models.ForeignKey(to='images.CustomImage', related_name='renditions')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='customrendition',
            unique_together=set([('image', 'filter_spec', 'focal_point_key')]),
        ),
    ]
