from django.contrib import admin
from .models import *

# Register your models here.
"""admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)"""

class OrderItemInline(admin.TabularInline):  # or use StackedInline for a different layout
    model = OrderItem
    extra = 1  # Provides an empty form for adding new items
    readonly_fields = ('item_subtotal',)  # Display subtotal in admin
    autocomplete_fields = ('product',)  # Enables search for products in admin

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('order_id', 'user__username')
    inlines = [OrderItemInline]  # Embed OrderItem management in Order admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'in_stock')
    search_fields = ('name',)
    list_filter = ('price',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)  # Optional: manage OrderItem separately if needed
