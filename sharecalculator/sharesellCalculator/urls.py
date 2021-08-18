from django.urls import path

from .import views


urlpatterns = [
    path('',views.index,name='sellShare'),
    path('sell_amount_details/',views.sell_calculate,name='sell_calculator'),
]