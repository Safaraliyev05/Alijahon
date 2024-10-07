from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AdminPageTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/admin-page/menu.html'
