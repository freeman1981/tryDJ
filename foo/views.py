from django.views.generic import ListView
from .models import Car


class CarList(ListView):
    model = Car
    context_object_name = 'list_of_cars'