from django.shortcuts import render
from .models import MenuCatagory
from .serializers import MenuCatagorySerializer

# Create your views here.

class MenuCatagoryListView(ListAPIView):
    queryset = MenuCatagory.objects.all()
    serializer_class = MenuCatagorySerializer