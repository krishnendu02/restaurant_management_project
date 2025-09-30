from rest_framework import serializers
from .models import MenuCatagory

class MenuCatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCatagory
        fields = ['name']