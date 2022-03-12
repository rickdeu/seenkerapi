from rest_framework.routers import DefaultRouter
from core import views
from django.urls import path, include

router=DefaultRouter()
router.register(r'category-list', views.CategoryViewSet)
router.register(r'product-list', views.ProductViewSet)
router.register(r'product-list-emphasis', views.ProductIsEmphasitViewSet)
router.register(r'banner-list', views.BannerViewSet)


app_name = 'core'
urlpatterns=[
    path('', include(router.urls)),
    path('product-details/<int:pk>/', views.productDetail, name='product-details'),
    path('product-by-category/<int:pk>/', views.productByCategory, name='product-by-category'),
    path('category-details/<int:pk>/', views.categoryDetail, name='category-details'),
    path('list-product-for-you/', views.listProductForYou, name='list-product-for-you'),
    path('most-popular-products/', views.mostPopularProduct, name='most-popular-products'),
    path('best-seller/', views.bestSeller, name='best-seller'),




]