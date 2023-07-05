from django.db import models

# Create your models here.

class sales(models.Model):
    CHOICES = [
        ('Food', (
            ('burger', 'hamburger'),
            ('pizza', 'pizza'),
            )
        ),
        
        ('Drink', (
            ('soda', 'soda'),
            ('water', 'water'),
            ('milk', 'milk'),
            ('beer', 'beer'),
            ),
        ),
        
        ('Dessert', (
            ('ic', 'ice-cream'),
            ('pie', 'pie'),
            ('cake', 'cake'),
            ),
        )
         
    ]
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=255, choices=CHOICES)
    description = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name  