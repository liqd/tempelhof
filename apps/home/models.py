from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail import blocks
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import InlinePanel
from wagtail.admin.panels import TitleFieldPanel
from wagtail.models import Orderable
from wagtail.models import Page
from wagtail.snippets.models import register_snippet

from apps.home.blocks import ColumnsListBlock
from apps.home.blocks import TeaserListBlock
from apps.home.blocks import UpdatesBlock
from apps.images.models import CustomImage
from apps.projects.blocks import CurrentProjectsListBlock


class HomePage(Page):
    image = models.ForeignKey(
        CustomImage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = fields.StreamField([
        ('text', blocks.RichTextBlock(icon='doc-full',
                                      template='home/blocks/text.html')),
        ('teasers', TeaserListBlock()),
        ('columns', ColumnsListBlock()),
        ('projects', CurrentProjectsListBlock()),
        ('updates', UpdatesBlock())
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('body'),
    ]

    parent_page_types = [
        'wagtailcore.Page'
    ]


class SimplePage(Page):
    body = fields.RichTextField(blank=True)

    content_panels = [
        TitleFieldPanel('title'),
        FieldPanel('body'),
    ]

    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = []


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.CASCADE
    )

    @property
    def url(self):
        return self.link_page.url

    def __str__(self):
        return self.title

    panels = [
        TitleFieldPanel('title'),
        FieldPanel('link_page')
    ]


@register_snippet
class NavigationMenu(ClusterableModel):
    title = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title

    panels = [
        TitleFieldPanel('title'),
        InlinePanel('items')
    ]


class NavigationMenuItem(Orderable, MenuItem):
    parent = ParentalKey('NavigationMenu', related_name='items')
