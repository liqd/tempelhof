import json

from django.core.serializers.json import DjangoJSONEncoder
from wagtail.wagtailcore import blocks

from apps.events.models import EventPage


class EventsTeaserBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        events = EventPage.objects.live()
        js_events = events.values('date', 'title', 'short_description')
        js_data = json.dumps(list(js_events), cls=DjangoJSONEncoder)

        context.update({
            'events': events,
            'js_data': js_data
        })

        return context

    class Meta:
        template = 'events/blocks/eventsteaser_block.html'
