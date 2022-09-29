from ast import Return
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    #permission_classes=[permissions.IsAuthenticated]

@api_view(['POST'])
def orderCreate(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



@api_view(['PUT'])
def orderUpdate(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except  Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def orderDetail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except  Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

@api_view(['DELETE'])
def orderDelete(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except  Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def orderByEmail(request, email):
    """try:
        order = Order.objects.filter(email=email)
    except  Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    """ 
    if request.method == 'GET':
        order = Order.objects.filter(email=email)
        serializer = OrderSerializer(order, many = True)
        return Response(serializer.data)



class OrderItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer
    #permission_classes=[permissions.IsAuthenticated]


@api_view(['POST'])
def orderItemCreate(request):
    if request.method == 'POST':
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



@api_view(['GET'])
def orderItemByOrder(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        orderItem = OrderItem.objects.filter(order=order)
    except  Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OrderItemSerializer(orderItem, many = True)
        return Response(serializer.data)

