from wagtail.wagtailcore import blocks


class LinkBlock(blocks.StructBlock):
    url = blocks.URLBlock()
    label = blocks.CharBlock()


class ArchiveBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()
    time = blocks.CharBlock()
    link = LinkBlock()
    documents = blocks.ListBlock(blocks.DocumentChooserBlock())

    class Meta:
        template = 'archive/blocks/archive_block.html'
