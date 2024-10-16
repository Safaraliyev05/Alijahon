from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models import Q, Count, Sum
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, DetailView, CreateView

from apps.forms import OrderCreateModelForm, StreamCreateModelForm
from apps.models import Product, Stream


class StreamListView(LoginRequiredMixin, ListView):
    model = Stream
    template_name = 'apps/admin-page/stream.html'
    context_object_name = 'streams'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(owner=self.request.user)
        return qs


class StreamProductDetailView(DetailView, CreateView):
    model = Stream
    template_name = 'apps/product/product-detail.html'
    form_class = OrderCreateModelForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['product'] = Product.objects.filter(pk=kwargs['object'].product.pk).first()
        ctx['stream'].visit_count += 1
        ctx['stream'].save()
        return ctx

    def form_valid(self, form):
        order = form.save()
        if len(form.cleaned_data['phone']) != 9:
            raise ValidationError('number must be 12 in length')
        return redirect('success_product', pk=order.pk)


class StreamCreateView(CreateView):
    model = Stream
    template_name = 'apps/admin-page/market.html'
    form_class = StreamCreateModelForm
    success_url = reverse_lazy('stream_list')

    def form_valid(self, form):
        stream = form.save(False)
        stream.owner = self.request.user
        stream.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class StreamStatusListView(ListView):
    model = Stream
    template_name = 'apps/admin-page/stats.html'
    context_object_name = 'streams'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(owner=self.request.user)

        if period := self.request.GET.get('period'):
            if period == 'today':
                qs = qs.filter(orders__created_at__exact=now().date())
            elif period == 'last_day':
                qs = qs.filter(orders__created_at__exact=now().date() - timedelta(1))
            elif period == 'weekly':
                qs = qs.filter(orders__created_at__gte=now() - timedelta(now().weekday()))
            elif period == 'monthly':
                qs = qs.filter(orders__created_at__year=now().year, orders__created_at__month=now().month)

        qs = qs.annotate(
            new=Count('orders', Q(orders__status='new')),
            ready=Count('orders', Q(orders__status='ready')),
            deliver=Count('orders', Q(orders__status='deliver')),
            delivered=Count('orders', Q(orders__status='delivered')),
            cant_phone=Count('orders', Q(orders__status='cant_phone')),
            canceled=Count('orders', Q(orders__status='canceled')),
            archived=Count('orders', Q(orders__status='archived'))
        )
        qs.aggregates = qs.aggregate(
            total_visit_count=Sum('visit_count'),
            total_new=Sum('new'),
            total_ready=Sum('ready'),
            total_deliver=Sum('deliver'),
            total_delivered=Sum('delivered'),
            total_cant_phone=Sum('cant_phone'),
            total_canceled=Sum('canceled'),
            total_archived=Sum('archived')
        )
        return qs
