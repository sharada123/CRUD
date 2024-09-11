from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobile=models.CharField(max_length=30)
    department=models.CharField(max_length=60)
    per=models.FloatField()