
from django.urls import path
import orders.views as views

app_name = 'orders'


urlpatterns = [
    path('create/',views.order_create,name='order_create'),
]