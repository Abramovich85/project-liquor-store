from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    count = models.IntegerField(default=0)

