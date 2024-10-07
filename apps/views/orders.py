from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count
from django.views.generic import ListView, DetailView

from apps.models import Order, SiteSettings
from apps.views.products import ProductListView


class OrderDetailView(DetailView):
    queryset = Order.objects.all()
    template_name = 'apps/order/success-product.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['delivery'] = SiteSettings.objects.first()
        return ctx


class OrderListView(LoginRequiredMixin, ListView):
    queryset = Order.objects.all()
    template_name = 'apps/order/order-list.html'
    context_object_name = 'orders'


class OrderStreamRequestListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'apps/admin-page/request.html'
    context_object_name = 'orders'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(stream__owner=self.request.user)

        return qs


class MarketListView(ProductListView):
    template_name = 'apps/admin-page/market.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if search := self.request.GET.get('search'):
            qs = qs.filter(Q(name__icontains=search) | Q(description__icontains=search))
        if category_slug := self.request.GET.get('category'):
            if category_slug == 'top':
                qs = qs.annotate(order_count=Count('order')).filter(
                    order__status=Order.StatusType.DELIVERED).order_by('-order_count', '-order__quantity')
            else:
                qs = qs.filter(category__slug=category_slug)
        return qs
