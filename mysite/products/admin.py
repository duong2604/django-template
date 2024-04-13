from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price", "brand","category", "image")

admin.site.register(Product,ProductAdmin)