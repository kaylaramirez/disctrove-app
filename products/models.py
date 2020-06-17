from django.db import models

# Create your models here.
from django.db import models

from common.constants import DISC_TYPES, STABILITY, SKILL_LEVEL


class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    manufacturer_name = models.CharField(max_length=30)

    def __str__(self):
        return self.manufacturer_name


# class Disc(model.Model):
    # disc_id = models.AutoField(primary_key=True)
    # manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # disc_name = models.
    # default_image
    # plastic = many


class Plastic(models.Model):
    plastic_id = models.AutoField(primary_key=True)
    plastic_type = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.plastic_type


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    disc = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=DISC_TYPES)
    image = models.ImageField(blank=True, upload_to='static/common/img/')
    stamp = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=250, blank=True)

    stability = models.CharField(max_length=30, choices=STABILITY)
    plastic_type = models.ForeignKey(Plastic, on_delete=models.PROTECT)
    plastic_grad = models.CharField(max_length=30)
    skill_level = models.CharField(max_length=30, choices=SKILL_LEVEL)

    #additional disc information
    #flight ratings
    speed = models.IntegerField()
    glide = models.IntegerField()
    turn = models.IntegerField()
    fade = models.IntegerField()

    color = models.CharField(max_length=30)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0, blank=True)

    #dimensions
    diameter = models.DecimalField(max_digits=5, decimal_places=1)
    height = models.DecimalField(max_digits=5, decimal_places=1)
    rim_depth = models.DecimalField(max_digits=5, decimal_places=1)
    rim_width = models.DecimalField(max_digits=5, decimal_places=1)
    manufacturer_weight = models.DecimalField(max_digits=5, decimal_places=2)
    scaled_weight = models.DecimalField(max_digits=5, decimal_places=2)

    collectors = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.disc

