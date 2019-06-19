from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.admin import edit_handlers
from wagtail.core import fields
from wagtail.core.models import Page
from wagtail.images import edit_handlers as image_handlers

from .blocks import ArchiveListBlock


class ArchivePage(Page):
    body = fields.StreamField([
        ('archive_list', ArchiveListBlock()),
    ])

    description = models.CharField(max_length=200)
    image = models.ForeignKey(
        'images.CustomImage',
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

    class Meta:
        verbose_name = _('Archive')

    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = []
