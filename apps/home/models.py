from django.db import models
from wagtail.wagtailadmin import blocks
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore import fields
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from apps.events.blocks import EventsTeaserBlock


class HomePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = fields.StreamField([
        ('events_list', EventsTeaserBlock(icon='date')),
        ('text', blocks.RichTextBlock())
    ])

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        edit_handlers.StreamFieldPanel('body'),
    ]
