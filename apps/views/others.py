from django.views.generic import TemplateView, ListView

from apps.models import Competition


class PaymentTemplateView(TemplateView):
    template_name = 'apps/admin-page/payment.html'


class CompetitionListView(ListView):
    model = Competition
    template_name = 'apps/admin-page/competition.html'
    context_object_name = 'competitions'
