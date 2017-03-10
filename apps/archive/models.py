from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore import fields
from wagtail.wagtailcore.models import Page

from .blocks import ArchiveListBlock


class ArchivePage(Page):
    body = fields.StreamField([
        ('archive_list', ArchiveListBlock()),
    ])

    content_panels = Page.content_panels + [
        edit_handlers.StreamFieldPanel('body'),
    ]

    parent_page_types = [
        'home.HomePage'
    ]
