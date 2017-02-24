from wagtail.wagtailadmin import blocks
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore import fields
from wagtail.wagtailcore.models import Page

from apps.events.blocks import EventsTeaserBlock


class HomePage(Page):
    body = fields.StreamField([
        ('events_list', EventsTeaserBlock(icon='date')),
        ('text', blocks.RichTextBlock())
    ])

    content_panels = Page.content_panels + [
        edit_handlers.StreamFieldPanel('body')
    ]
