from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from .blocks import ArchiveListBlock


class ArchivePage(Page):
    body = fields.StreamField([
        ('archive_list', ArchiveListBlock()),
    ], use_json_field=True)

    description = models.CharField(max_length=200)
    image = models.ForeignKey(
        'images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('image'),
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = _('Archive')

    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = []
