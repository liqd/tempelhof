from wagtail.wagtailadmin import blocks

from apps.events.models import EventPage


class EventsTeaserBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    count = blocks.IntegerBlock(min_value=2,
                                help_text='How many events should be '
                                          'shown?')

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update({
            'events': EventPage.objects.live()[:value['count']]
        })

        return context

    class Meta:
        template = 'events/blocks/eventsteaser_block.html'
