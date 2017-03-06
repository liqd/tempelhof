from django import template

from apps.home.models import NavigationMenu

register = template.Library()


@register.assignment_tag
def get_menu(title):
    menu = NavigationMenu.objects.filter(title=title).first()

    if menu is not None:
        return menu.items.all()
