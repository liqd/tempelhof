# Generated by Django 3.2.16 on 2022-12-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_customimage_file_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customimage',
            name='file_hash',
            field=models.CharField(blank=True, db_index=True, editable=False, max_length=40),
        ),
    ]