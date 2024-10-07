from django.views.generic import DetailView, TemplateView

from apps.models import Competition


class PaymentTemplateView(TemplateView):
    template_name = 'apps/admin-page/payment.html'


class CompetitionListView(DetailView):
    model = Competition
    template_name = 'apps/admin-page/competition.html'

    def get_object(self, queryset=None):
        return '1'
