from django.db import models
# Create your models here.


class AllProducts(models.Model):
    product_name = models.CharField(max_length=500, default="",null=True)
    product_quantity = models.CharField(max_length=1000, default="", null=True)
    product_price = models.CharField(max_length=500, default=None, null=True)
    product_description = models.CharField(max_length=200, default=None, null=True)
