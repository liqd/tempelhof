from wagtail.wagtailcore import blocks
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class DocsBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    images = blocks.ListBlock(ImageChooserBlock())
    documents = blocks.ListBlock(DocumentChooserBlock())

    class Meta:
        template = 'docs/blocks/docs_block.html'
