from django.db import models

from products.models import Product
from datetime import datetime


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


#class CartItem(models.Model):
#    cartItem_id = models.AutoField(primary_key=True)
#    product_item = models.ForeignKey(Product, on_delete=models.CASCADE)
