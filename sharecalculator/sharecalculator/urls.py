
import sharebuyCalculator , sharesellCalculator
from django.contrib import admin
from django.urls import path , include
from .import views

urlpatterns = [
    path('',views.index,name='home'),
    path('share-buy-calculator/',include('sharebuyCalculator.urls')),
    path('share-sell-calculator/',include('sharesellCalculator.urls')),
    path('admin/', admin.site.urls),
    
    
]
