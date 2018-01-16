from django.utils import timezone
from wagtail.wagtailcore import blocks

from apps.events.models import EventPage


class EventsTeaserBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    calendar_link_text = blocks.CharBlock(required=False)
    calendar_link = blocks.PageChooserBlock(
        required=False,
        target_model='events.CalendarPage'
    )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        events = EventPage.objects.live()

        events = events.filter(date__gte=timezone.now())
        events = events.order_by('date', 'time_start')

        if events and events.count() >= 5:
            events = events[:5]

        context.update({
            'events': events
        })

        return context

    class Meta:
        template = 'events/blocks/eventsteaser_block.html'
