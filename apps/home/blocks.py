from wagtail.wagtailcore import blocks

from apps.contrib.blocks import IconBlock


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
