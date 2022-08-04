from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    birth= models.DateField()