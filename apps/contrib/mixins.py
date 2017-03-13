from django.core.paginator import Paginator


class PaginatorMixin:
    objects_per_page = 10

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        objects = self.get_children().live().specific()
        paginator = Paginator(objects, self.objects_per_page)
        page_number = request.GET.get('p', 1)

        context.update({
            'paginator_page': paginator.page(page_number),
        })

        return context
