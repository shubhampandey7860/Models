from django.db import models

# Create your models here.
class Employee(models.Model):
    Ename=models.CharField(max_length=20)
    EmpId=models.IntegerField()
    salary=models.IntegerField()
