from turtle import position
from django.db import models

# Create your models here.
class Employee_model(models.Model):
    empname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    occupation = models.CharField(max_length=150)
    salary = models.IntegerField()
    gender = models.CharField(max_length=1)
    class Meta:
        db_table = "employee_details"

    
