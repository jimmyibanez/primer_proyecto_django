from operator import truediv
from django.db import models


# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    ##user_created= models.DateField(auto_now_add= True, null=True, blank= True)
    