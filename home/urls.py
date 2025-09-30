from django.urls import path
from .views import *

urlpatterns = [
    path('catagories/', MenuCategoryListView.as_view(), name = 'menu-catagories')
]