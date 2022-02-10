from django.db import models
from django.http import request 

# Create your models here.
class contact(models.Model):
    name =models.CharField(max_length=25)
    phone= models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    