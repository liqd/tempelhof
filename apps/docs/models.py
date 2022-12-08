from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from .blocks import DocsBlock


class DocsPage(Page):
    body = fields.StreamField([
        ('documents_list', DocsBlock())
    ], use_json_field=True)

    description = models.CharField(max_length=200)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = _('Documents')

    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = []
