from wagtail.wagtailcore import blocks
from wagtail.wagtaildocs.blocks import DocumentChooserBlock


class DocsBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    documents = blocks.ListBlock(DocumentChooserBlock())

    class Meta:
        template = 'docs/blocks/docs_block.html'
