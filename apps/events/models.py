from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page

from apps.contrib.mixins import PaginatorMixin


class CalendarPage(PaginatorMixin, Page):
    objects_per_page = 12

    def get_ordered_children(self):
        return EventPage.objects.descendant_of(self).order_by('date')

    class Meta:
        verbose_name = _('Calendar')

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

    short_description = models.CharField(max_length=112,
                                         help_text='Shown on the homepage.')
    description = RichTextField()

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

    class Meta:
        verbose_name = _('Event')

    parent_page_types = [
        'events.CalendarPage'
    ]
    subpage_types = []
