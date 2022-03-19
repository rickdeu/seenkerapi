from rest_framework import serializers
from .models import *
import datetime
import time
#from datetime import datetime

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
        s1 = f"{obj.open}" #.strftime("%H:%M:%S")
        s2 = f"{obj.close}"#.strftime("%H:%M:%S")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        s3 = f"{current_time}"
        d1 = datetime.datetime.strptime(s1, '%H:%M:%S')
        d2 = datetime.datetime.strptime(s2, '%H:%M:%S')
        d3 = datetime.datetime.strptime(s3,'%H:%M:%S')
        if(d1<=d3 and d2>=d3):
            isOpen = 1
        else:
            isOpen = 0
        return isOpen

