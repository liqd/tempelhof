from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore import fields
from wagtail.wagtailcore.models import Page

from .blocks import ArchiveBlock


class ArchivePage(Page):
    body = fields.StreamField([
        ('archive_list', ArchiveBlock()),
    ])

    content_panels = Page.content_panels + [
        edit_handlers.StreamFieldPanel('body'),
    ]
