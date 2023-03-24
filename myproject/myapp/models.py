from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PersonalDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20,default='phone_number')
    date_of_birth = models.CharField(max_length=50,default='00/00/0000')
    gender = models.CharField(max_length=10,default='gender')
    city = models.CharField(max_length=50,default='city')