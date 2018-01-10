from django import template
from django.utils import timezone

from apps.events.models import EventPage

register = template.Library()


@register.assignment_tag
def get_upcoming_events():
    events = EventPage.objects.live()
    events = events.filter(date__gte=timezone.now())
    events = events.order_by('date', 'time_start')

    if events:
        if events.count() >= 5:
            return events[:5]
        else:
            return events
    else:
        return None
