from django.db import models

class Employees(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    contact=models.PositiveIntegerField()
    
