from django.urls import path

from orders.views import OrderView, CreateOrderProductView


urlpatterns = [
    path('detail/', OrderView.as_view(), name='orders.detail'),
    path('add/', CreateOrderProductView.as_view(), name='orders.add'),
]