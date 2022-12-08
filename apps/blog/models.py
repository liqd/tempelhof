from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail import fields as wagtail_fields
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from apps.contrib.mixins import PaginatorMixin


class BlogIndexPage(PaginatorMixin, Page):
    description = models.CharField(max_length=200)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]

    class Meta:
        verbose_name = _('Blog')

    parent_page_types = [
        'home.HomePage'
    ]

    subpage_types = [
        'blog.BlogEntryPage'
    ]


class BlogEntryPage(Page):
    text = wagtail_fields.RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('text'),
    ]

    class Meta:
        verbose_name = _('Blog Entry')

    parent_page_types = [
        'blog.BlogIndexPage'
    ]
    subpage_types = []
