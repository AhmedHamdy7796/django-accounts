from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(max_length=2)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    addres = models.CharField(max_length=50, null=True, blank=True)
    experience = models.CharField(max_length=200, null= True, blank=True) 
