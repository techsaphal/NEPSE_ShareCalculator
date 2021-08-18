from django.urls import path

from .import views


urlpatterns = [
    path('',views.index,name='buyShare'),
    path('buy_amount_details/',views.buy_calculate,name='buy_calculator'),
]