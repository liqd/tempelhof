# Generated by Django 2.2.2 on 2019-06-21 09:01

import apps.home.blocks
import apps.projects.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20190621_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock(icon='doc-full', template='home/blocks/text.html')), ('teasers', wagtail.core.blocks.StructBlock([('teasers', wagtail.core.blocks.ListBlock(apps.home.blocks.TeaserBlock))])), ('columns', wagtail.core.blocks.StructBlock([('columns', wagtail.core.blocks.ListBlock(apps.home.blocks.ColumnBlock))])), ('projects', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('projects', wagtail.core.blocks.ListBlock(apps.projects.blocks.CurrentProjectBlock, help_text='Chose one or more Project Pages. Other pagetypes will result in an error.', target_model='projects.ProjectPage'))])), ('updates', wagtail.core.blocks.StructBlock([('status', wagtail.core.blocks.PageChooserBlock(page_type=['blog.BlogEntryPage'])), ('calendar', wagtail.core.blocks.StructBlock([('calendar_link_text', wagtail.core.blocks.CharBlock(required=False)), ('calendar_link', wagtail.core.blocks.PageChooserBlock(page_type=['events.CalendarPage'], required=False))]))]))]),
        ),
    ]