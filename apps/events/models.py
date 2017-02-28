from django.db import models
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page


class CalendarPage(Page):
    pass


class EventPage(Page):
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()

    short_description = models.CharField(max_length=56,
                                         help_text='Shown on the homepage.')
    description = RichTextField(max_length=512)

    content_panels = Page.content_panels + [
        edit_handlers.MultiFieldPanel([
            edit_handlers.FieldPanel('date'),
            edit_handlers.FieldRowPanel(
                [
                    edit_handlers.FieldPanel('time_start'),
                    edit_handlers.FieldPanel('time_end')
                ]
            ),
        ], heading='Date and Time'),

        edit_handlers.MultiFieldPanel([
            edit_handlers.RichTextFieldPanel('description'),
            edit_handlers.FieldPanel('short_description'),
        ], heading='Text'),
    ]

    parent_page_types = [
        'events.CalendarPage'
    ]
