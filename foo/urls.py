from django.conf.urls import url

from .views import CarList

urlpatterns = [
    url(r'^$', CarList.as_view(), name='car_list'),
]