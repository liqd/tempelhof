from django.forms import ChoiceField
from wagtail.wagtailcore.blocks import FieldBlock

icons = [
    {'classname': 'fa-archive', 'name': 'Archive'},
    {'classname': 'fa-file', 'name': 'Document'},
    {'classname': 'fa-users', 'name': 'Participation'},
    {'classname': 'fa-download', 'name': 'Download'},
    {'classname': 'fa-book', 'name': 'Book'},
    {'classname': 'section', 'name': 'Paragraph'},
]


class IconBlock(FieldBlock):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.field = ChoiceField(choices=[
            (icon['classname'], icon['name']) for icon in icons
        ])
