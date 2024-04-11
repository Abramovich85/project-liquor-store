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
    filter_vertical = ('category',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('_id', 'user', 'status', 'total_price',
                    'created_at', 'updated_at')

    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name'
    )

    fields = ('user', 'status')

    list_filter = ('status', 'created_at', 'updated_at')

    actions = ['cancel_order', 'set_payed', 'set_in_progress']

    def cancel_order(self, request, queryset):
        queryset.update(status=Order.Status.CANCELED)
    cancel_order.short_description = 'Отменить выбранные заказы'

    def set_payed(self, request, queryset):
        queryset.update(status=Order.Status.PAYED)
    set_payed.short_description = 'Сделать заказы оплаченными'

    def set_in_progress(self, request, queryset):
        queryset.update(status=Order.Status.IN_PROGRESS)
    set_in_progress.short_description = 'Сделать заказы в обработке'

    @admin.display(description='№')
    def _id(self, obj):
        return obj.pk

    @admin.display(description='Сумма')
    def total_price(self, obj):
        return obj.total_price
