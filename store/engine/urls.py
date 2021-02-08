from django.urls import path
from .views import *

urlpatterns = [
    path('', items_list, name='index_url'),
    path('checkout/', checkout, name='checkout_url'),
    path('product/', product, name='product_url'),

]