from django.urls import path
from .views import *

urlpatterns = [
    path('catagories/', MenuCatagorylistView.as_view(), name = 'menu-catagories')
]