from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock


class LinkBlock(blocks.StructBlock):
    url = blocks.URLBlock()
    label = blocks.CharBlock()


class ArchiveBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()
    time = blocks.CharBlock()
    link = LinkBlock()
    documents = blocks.ListBlock(DocumentChooserBlock())

    class Meta:
        template = 'archive/blocks/archive_block.html'


class ArchiveListBlock(blocks.StructBlock):
    archives = blocks.ListBlock(ArchiveBlock())

    class Meta:
        template = 'archive/blocks/archivelist_block.html'
