from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class ProjectIndexPage(Page):
    class Meta:
        verbose_name = _('Project Containers')

    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = [
        'ProjectContainerPage'
    ]


class ProjectContainerPage(Page):
    image = models.ForeignKey(
        'images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    short_description = models.CharField(max_length=112,
                                         help_text=_('Shown in list.'))
    description = fields.RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('short_description'),
        FieldPanel('description'),
        FieldPanel('image'),
    ]

    class Meta:
        verbose_name = _('Project Container')

    parent_page_types = [
        'ProjectIndexPage'
    ]
    subpage_types = [
        'ProjectPage'
    ]


class ProjectPage(Page):
    image = models.ForeignKey(
        'images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    start_date = models.DateField()
    end_date = models.DateField()

    short_description = models.CharField(max_length=112,
                                         help_text=_('Shown in list.'))
    description = fields.RichTextField()
    embed_code = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('short_description'),
        FieldPanel('description'),
        FieldPanel('image'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('embed_code'),
    ]

    class Meta:
        verbose_name = _('Project')

    parent_page_types = [
        'ProjectContainerPage'
    ]
    subpage_types = []
