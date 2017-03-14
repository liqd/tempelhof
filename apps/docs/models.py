from django.db import models
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore import fields
from wagtail.wagtailcore.models import Page

from .blocks import DocsBlock


class DocsPage(Page):
    body = fields.StreamField([
        ('documents_list', DocsBlock())
    ])

    description = models.CharField(max_length=200)

    content_panels = Page.content_panels + [
        edit_handlers.FieldPanel('description'),
        edit_handlers.StreamFieldPanel('body'),
    ]

    parent_page_types = [
        'home.HomePage'
    ]
