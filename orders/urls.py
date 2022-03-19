from turtle import update
from rest_framework.routers import DefaultRouter
from orders import views
from django.urls import path, include

router=DefaultRouter()
router.register(r'orders-list', views.OrderViewSet)
router.register(r'orders-item-list', views.OrderItemViewSet)
#router.register(r'orders-item-create', views.orderCreate)


app_name = 'orders'
urlpatterns=[
    path('', include(router.urls)),
    path('orders-item-create/', views.orderCreate, name='orders-item-create'),
    path('orders-item-update/<int:pk>/', views.orderUpdate, name='orders-item-update'),
    path('orders-item-details/<int:pk>/', views.orderDetail, name='orders-item-details'),
    path('orders-item-delete/<int:pk>/', views.orderDelete, name='orders-item-delete'),
    path('orders-by-mail/<str:mail>/', views.orderByEmail, name='orders-by-mail'),
    path('orders-item-by-order/<int:pk>/', views.orderItemByOrder, name='order-item-by-order'),
    path('order-details-create', views.orderItemCreate, name='order-details-create'),

]