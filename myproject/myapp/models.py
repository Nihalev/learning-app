from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PersonalDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=50)
    gender= models.CharField(max_length=10)
    city= models.CharField(max_length=50)
    image= models.FileField(upload_to='images', default='images\default.png')