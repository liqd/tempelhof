from wagtail.wagtailcore import blocks


class TeaserBlock(blocks.StructBlock):
    text = blocks.RichTextBlock()
    button_text = blocks.CharBlock()
    button_link = blocks.PageChooserBlock()
    icon = blocks.ChoiceBlock([
        ('users', 'Participation'),
        ('file', 'Document'),
        ('archive', 'Archive'),
    ])

    class Meta:
        template = 'home/blocks/teaser_block.html'


class TeaserListBlock(blocks.StructBlock):
    teasers = blocks.ListBlock(TeaserBlock)

    class Meta:
        template = 'home/blocks/teaserlist_block.html'
