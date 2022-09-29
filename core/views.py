from ast import Return
from itertools import product
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Count

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    #permission_classes=[permissions.IsAuthenticated]

class ProductIsEmphasitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Product.objects.filter(isEmphasi=True).order_by('-id')[:10]
    serializer_class=ProductSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Product.objects.order_by('-id')[:10]
    serializer_class=ProductSerializer



@api_view(['GET'])
def categoryDetail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except  Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['GET'])
def productDetail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except  Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

@api_view(['GET'])
def productByCategory(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        product = Product.objects.filter(category=category)
    except  Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product, many = True)
        return Response(serializer.data)


class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Banner.objects.filter(isActive=True)
    serializer_class=BannerSerializer
    #permission_classes=[permissions.IsAuthenticated]
class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Store.objects.all()
    serializer_class=StoreSerializer
    #permission_classes=[permissions.IsAuthenticated]


@api_view(['GET'])
def listProductForYou(request):
    context = {
        'request': request
    }
    if request.method == 'GET':
        products = Product.objects.all()#[:10]
        serializer = ProductSerializer(products, many=True, context=context)
        return Response(serializer.data)

@api_view(['GET'])
def mostPopularProduct(request):
    #popular_events = Events.objects.annotate(attendee_count=Count('attendee')).filter(attendee_count__gt=50)
    
    context = {
        'request': request
    }
    if request.method == 'GET':
        products = Product.objects.all()#[:10]#.annotate(product_count=Count('order_items__product__id')).filter(product_count__gt=10) 
        serializer = ProductSerializer(products, many=True, context=context)
        return Response(serializer.data)

@api_view(['GET'])
def bestSeller(request):
    context = {
        'request': request
    }
    if request.method == 'GET':
        products = Product.objects.all()#[:10]
        serializer = ProductSerializer(products, many=True, context=context)
        return Response(serializer.data)