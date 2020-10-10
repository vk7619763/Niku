from django.db import models

# Create your models here.
class employee(models.Model):
    ename=models.CharField(max_length=30)
    eno=models.IntegerField()
    esal=models.IntegerField()
    ecity=models.CharField(max_length=30)
