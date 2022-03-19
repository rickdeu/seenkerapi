from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    isOpen = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Store
        fields = ['id','name','phone','email', 'description', 'address', 'lat', 'log', 'image', 'open', 'close', 'created_at', 'isOpen']
    
    def get_isOpen(self, obj):
        isOpen = 1
        return isOpen
