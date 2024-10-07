from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView

from apps.models import Favourite


class FavouriteView(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        obj, created = Favourite.objects.get_or_create(user=request.user, product_id=pk)
        if not created:
            obj.delete()
        referer = request.META.get('HTTP_REFERER')
        if referer:
            return redirect(referer)


class FavouriteListView(LoginRequiredMixin, ListView):
    model = Favourite
    template_name = 'apps/admin-page/favourite.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
