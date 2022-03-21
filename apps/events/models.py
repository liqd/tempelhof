import json

from django.core import paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from wagtail.admin import edit_handlers
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class CalendarPage(Page):
    objects_per_page = 12

    class Meta:
        verbose_name = _('Calendar')

    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = [
        'events.EventPage'
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        events = EventPage.objects.live().descendant_of(self)
        js_events = events.values('date', 'title', 'short_description')
        js_data = json.dumps(list(js_events), cls=DjangoJSONEncoder)

        dates = request.GET.get('dates', 'upcoming')

        if dates == 'upcoming':
            events = events.filter(date__gte=timezone.now())
        elif dates == 'past':
            events = events.filter(date__lt=timezone.now())

        events = events.order_by('date', 'time_start')

        paginator_obj = paginator.Paginator(events, self.objects_per_page)
        page_number = request.GET.get('p', 1)

        try:
            page = paginator_obj.page(page_number)
        except paginator.PageNotAnInteger:
            page = paginator_obj.page(1)
        except paginator.EmptyPage:
            page = paginator_obj.page(paginator_obj.num_pages)

        context.update({
            'js_data': js_data,
            'js_events': EventPage.objects.live().descendant_of(self),
            'events': events,
            'paginator_page': page,
        })

        return context


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
