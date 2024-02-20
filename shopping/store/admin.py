from django.contrib import admin

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display=['id','name','price','category','description']

from .models.product import Product
from .models.category import Category

admin.site.register(Product,AdminProduct)
admin.site.register(Category)