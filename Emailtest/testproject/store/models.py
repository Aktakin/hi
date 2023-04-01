from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    inventory = models.IntegerField()
    is_available = models.BooleanField()

    def __str__(self) -> str:
        return self.title
    
    
