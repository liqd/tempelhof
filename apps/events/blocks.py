from wagtail.wagtailcore import blocks


class EventsTeaserBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    calendar_link_text = blocks.CharBlock(required=False)
    calendar_link = blocks.PageChooserBlock(
        required=False,
        target_model='events.CalendarPage'
    )

    class Meta:
        template = 'events/blocks/eventsteaser_block.html'
