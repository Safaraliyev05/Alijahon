from django.db.models import Q
from django.views.generic import ListView

from apps.models import Product, Category


class CategoryListView(ListView):
    model = Product
    template_name = 'apps/product/category-list.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx['categories'] = Category.objects.all()
        return ctx

    def get_queryset(self):
        qs = super().get_queryset()
        if search := self.request.GET.get('search'):
            qs = qs.filter(Q(name__icontains=search) | Q(description__icontains=search))
        return qs


# 5
class CategoryObjectListView(ListView):
    model = Product
    template_name = 'apps/product/category-list.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        if slug := self.kwargs.get('slug'):
            qs.filter(category__slug=slug)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx['categories'] = Category.objects.all()
        return ctx
