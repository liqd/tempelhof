from django.db import models
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page


class CalendarPage(Page):
    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = [
        'events.EventPage'
    ]


class EventPage(Page):
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    place = models.CharField(max_length=32)
    contact = models.EmailField()

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
            edit_handlers.FieldPanel('place'),
            edit_handlers.FieldPanel('contact'),
        ], heading='Key Data'),

        edit_handlers.MultiFieldPanel([
            edit_handlers.RichTextFieldPanel('description'),
            edit_handlers.FieldPanel('short_description'),
        ], heading='Text'),
    ]

    parent_page_types = [
        'events.CalendarPage'
    ]
    subpage_types = []
