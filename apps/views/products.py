from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView

from apps.forms import OrderCreateModelForm
from apps.models import Product, Category, Stream


class ProductListView(ListView):
    model = Product
    template_name = 'apps/product/product-list.html'
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


# 2
class ProductDetailCreateView(DetailView, CreateView):
    model = Product
    template_name = 'apps/product/product-detail.html'
    form_class = OrderCreateModelForm
    context_object_name = 'product'

    def form_valid(self, form):
        order = form.save()
        if len(form.cleaned_data['phone']) != 9:
            raise ValidationError('number must be 12 in length')
        return redirect('success_product', pk=order.pk)


# 3
class ProductStatisticDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'apps/product/product-statistics.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        streams = Stream.objects.filter(product=ctx['product'])
        ctx['all_stream_len'] = streams.count()
        ctx['user_stream_len'] = streams.filter(owner=self.request.user).count()

        return ctx
