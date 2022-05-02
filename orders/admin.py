from django.contrib import admin
from .models import Order ,OrderItem
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','paid','created','updated']
    list_filter = ['paid',]
    inlines = [OrderItemInline]