# Generated by Django 4.2 on 2024-06-24 09:54

from django.db import migrations
import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_alter_customimage_file_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customimage',
            name='file',
            field=wagtail.images.models.WagtailImageField(height_field='height', upload_to=wagtail.images.models.get_upload_to, verbose_name='file', width_field='width'),
        ),
        migrations.AlterField(
            model_name='customrendition',
            name='file',
            field=wagtail.images.models.WagtailImageField(height_field='height', storage=wagtail.images.models.get_rendition_storage, upload_to=wagtail.images.models.get_rendition_upload_to, width_field='width'),
        ),
    ]
