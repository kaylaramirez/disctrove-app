from django.contrib import admin

# Register your models here.
from products.models import Product, Manufacturer, Plastic


#admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Plastic)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['disc', 'manufacturer', 'plastic_type', ]
    # list_filter = []
    # search_fields = []
