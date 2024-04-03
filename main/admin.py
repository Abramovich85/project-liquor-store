from django.contrib import admin

from .models import Order, Product, Categories
# Register your models here.

# admin.site.register(Product)
# admin.site.register(Categories)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Order)