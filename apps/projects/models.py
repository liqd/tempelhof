from django.db import models
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class ProjectIndexPage(Page):
    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = [
        'ProjectPage'
    ]


class ProjectPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    start_date = models.DateField()
    end_date = models.DateField()

    description = models.CharField(max_length=256)
    link = models.URLField()

    content_panels = Page.content_panels + [
        edit_handlers.FieldPanel('description'),
        ImageChooserPanel('image'),
        edit_handlers.FieldPanel('start_date'),
        edit_handlers.FieldPanel('end_date'),
        edit_handlers.FieldPanel('link'),
    ]

    parent_page_types = [
        'ProjectIndexPage'
    ]
