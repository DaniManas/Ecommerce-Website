from django.db import models
from django.db.models.base import Model

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=250)
    pub_date=models.DateField()