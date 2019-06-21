from wagtail.core import blocks

from apps.projects.models import ProjectPage


class CurrentProjectBlock(blocks.PageChooserBlock):
    target_model = ProjectPage

    class Meta:
        template = 'projects/blocks/project_block.html'


class CurrentProjectsListBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    projects = blocks.ListBlock(
        CurrentProjectBlock,
        target_model='projects.ProjectPage'
    )

    class Meta:
        template = 'projects/blocks/projectslist_block.html'
