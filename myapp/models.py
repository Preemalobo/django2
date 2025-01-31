from django.db import models

# Create your models here.

class Items(models.Model):
    name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=6,decimal_places=2,null=True)
    description=models.TextField(default="This is Description")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
