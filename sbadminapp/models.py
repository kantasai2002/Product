from django.db import models

# Create your models here.
class Customer(models.Model):
    cname=models.CharField(max_length=100)
    uemail=models.EmailField(max_length=100)
    address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)

class Meta:
    db_table="customer"