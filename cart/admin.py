from django.contrib import admin

# Register your models here.
from cart.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'created_at', ]
