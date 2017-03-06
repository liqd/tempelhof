from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.wagtailadmin import blocks
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore import fields
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsnippets.models import register_snippet

from apps.events.blocks import EventsTeaserBlock


class HomePage(Page):
    body = fields.StreamField([
        ('events_list', EventsTeaserBlock(icon='date')),
        ('text', blocks.RichTextBlock())
    ])

    content_panels = Page.content_panels + [
        edit_handlers.StreamFieldPanel('body')
    ]


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    link_page = models.ForeignKey('wagtailcore.Page')

    @property
    def url(self):
        return self.link_page.url

    def __str__(self):
        return self.title

    panels = [
        edit_handlers.FieldPanel('title'),
        edit_handlers.PageChooserPanel('link_page')
    ]


@register_snippet
class NavigationMenu(ClusterableModel):
    title = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title

    panels = [
        edit_handlers.FieldPanel('title'),
        edit_handlers.InlinePanel('items')
    ]


class NavigationMenuItem(Orderable, MenuItem):
    parent = ParentalKey('NavigationMenu', related_name='items')
