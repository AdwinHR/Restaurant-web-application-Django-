
from django.db import models
from django.http import request 

# Create your models here.
class contact(models.Model):
    name =models.CharField(max_length=25)
    email= models.EmailField()
    phone=models.PositiveBigIntegerField()
    address=models.CharField(max_length=125)
    selected =models.CharField(max_length=500)
    amount= models.IntegerField(max_length=25)
    def __str__(self):
        return self.name
    
class reserve_table(models.Model):
    name1 =models.CharField(max_length=25)
    email1= models.EmailField()
    phone1=models.PositiveBigIntegerField()   
    tables_count=models.PositiveIntegerField()
    date=models.CharField(max_length=25)
    time=models.CharField(max_length=25)
    def __str__(self):
        return self.name1