from django.contrib import admin
from core.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image',)

class ProductInline(admin.TabularInline):
    model = Product


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    inlines = [ProductInline]
    resource_class = CategoryResource
    list_display = ('name', 'image', )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'image', 'avaliable', 'created_at' )

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'isActive', 'description' )


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'lat', 'log', 'open',  'close' )
    save_as = True

