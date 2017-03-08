from wagtail.wagtailcore import blocks
from wagtail.wagtailimages import blocks as image_blocks


class CurrentProjectBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    description = blocks.CharBlock()
    image = image_blocks.ImageChooserBlock()
    date_start = blocks.DateBlock()
    date_end = blocks.DateBlock()
    link = blocks.URLBlock()

    class Meta:
        template = 'projects/blocks/project_block.html'


class CurrentProjectsListBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    projects = blocks.ListBlock(CurrentProjectBlock)

    class Meta:
        template = 'projects/blocks/projectslist_block.html'
