#from typing_extensions import TypeGuard
from django.db import models

# Create your models here.
class Employclass(models.Model):
   
    empid=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Companyclass(models.Model):
   jobid=models.CharField(max_length=100)
   jobprofile=models.CharField(max_length=100)
   salary=models.CharField(max_length=100)
   employid=models.CharField(primary_key=True,max_length=100)
   def __str__(self):
        return self.jobid

