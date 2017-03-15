from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore import fields as wagtail_fields
from wagtail.wagtailcore.models import Page

from apps.contrib.mixins import PaginatorMixin


class BlogIndexPage(PaginatorMixin, Page):
    description = models.CharField(max_length=200)

    content_panels = Page.content_panels + [
        edit_handlers.FieldPanel('description'),
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
        edit_handlers.RichTextFieldPanel('text'),
    ]

    class Meta:
        verbose_name = _('Blog Entry')

    parent_page_types = [
        'blog.BlogIndexPage'
    ]
    subpage_types = []
