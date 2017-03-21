from wagtail.wagtailcore import blocks

from apps.contrib.blocks import IconBlock
from apps.events.blocks import EventsTeaserBlock


class TeaserBlock(blocks.StructBlock):
    text = blocks.RichTextBlock()
    button_text = blocks.CharBlock()
    button_link = blocks.PageChooserBlock()
    icon = IconBlock()

    class Meta:
        template = 'home/blocks/teaser_block.html'


class TeaserListBlock(blocks.StructBlock):
    teasers = blocks.ListBlock(TeaserBlock)

    class Meta:
        template = 'home/blocks/teaserlist_block.html'


class ColumnBlock(blocks.StructBlock):
    icon = IconBlock()
    title = blocks.CharBlock()
    text = blocks.RichTextBlock()

    class Meta:
        template = 'home/blocks/column_block.html'


class UpdatesBlock(blocks.StructBlock):
    status = blocks.PageChooserBlock(target_model='blog.BlogEntryPage')
    calendar = EventsTeaserBlock()

    class Meta:
        template = 'home/blocks/updates_block.html'


class ColumnsListBlock(blocks.StructBlock):
    columns = blocks.ListBlock(ColumnBlock)

    class Meta:
        template = 'home/blocks/columnslist_block.html'
