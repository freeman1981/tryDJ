from django.views.generic import ListView
from django.shortcuts import get_list_or_404

from .models import Car


class CarList(ListView):
    context_object_name = 'list_of_cars'
    template_name = 'foo/car_list.html'

    def get_queryset(self):
        return get_list_or_404(Car, name=self.args[0])