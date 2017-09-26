from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore import fields
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


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
        edit_handlers.FieldPanel('short_description'),
        edit_handlers.FieldPanel('description'),
        ImageChooserPanel('image'),
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
        edit_handlers.FieldPanel('short_description'),
        edit_handlers.FieldPanel('description'),
        ImageChooserPanel('image'),
        edit_handlers.FieldPanel('start_date'),
        edit_handlers.FieldPanel('end_date'),
        edit_handlers.FieldPanel('embed_code'),
    ]

    class Meta:
        verbose_name = _('Project')

    parent_page_types = [
        'ProjectContainerPage'
    ]
    subpage_types = []
