from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class DocsBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    images = blocks.ListBlock(ImageChooserBlock())
    body = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'docs/blocks/docs_block.html'
