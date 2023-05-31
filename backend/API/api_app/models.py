from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Item(models.Model):
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self) -> str:
        return f"{self.name}"
    
    
    
    
