from django.urls import path
from .views import *

urlpatterns = [
    path('catagories/', MenuCatagorieslistView.as_view(), name = 'menu-catagories')
]