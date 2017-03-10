from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailimages import edit_handlers as image_handlers
from wagtail.wagtailcore import fields
from django.db import models
from wagtail.wagtailcore.models import Page

from .blocks import ArchiveListBlock


class ArchivePage(Page):
    body = fields.StreamField([
        ('archive_list', ArchiveListBlock()),
    ])

    description = models.CharField(max_length=200)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        edit_handlers.FieldPanel('description'),
        image_handlers.ImageChooserPanel('image'),
        edit_handlers.StreamFieldPanel('body'),
    ]

    parent_page_types = [
        'home.HomePage'
    ]
