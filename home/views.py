from django.shortcuts import render

# Create your views here.


class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuCatagoryListView(ListAPIView):
    queryset = MenuCatagory.objects.all()
    serializer_class = MenuCatagorySerializer