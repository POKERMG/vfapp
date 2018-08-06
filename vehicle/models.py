from django.db import models
from django.contrib.auth.models import User

# Various Models that are within the project

# Creation of model for user profiles

class UserProfile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=100, default='')
    city        = models.CharField(max_length=100, default='')
    phone       = models.IntegerField(default=0)
    type        = models.CharField(max_length=20, default='client')

# Creation of model for cars

class Car(models.Model):
    vehicleId           = models.CharField(max_length=20, null=False)
    make                = models.CharField(max_length=40)
    shortModel          = models.CharField(max_length=35)
    longModel           = models.TextField()
    trim                = models.CharField(max_length=35)
    derivative          = models.CharField(max_length=35)
    yearIntroduced      = models.CharField(max_length=5)
    yearDiscontinued    = models.CharField(max_length=5, null=True)
    currentlyAvailable  = models.CharField(max_length=10, default="Y")
    model_pic           = models.ImageField(upload_to='media', default='default.jpeg')
    owner               = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)

# Creation of model for contact messages

class ContactMessage(models.Model):
    name    = models.CharField(max_length=30)
    phone   = models.CharField(max_length=13)
    email   = models.EmailField(max_length=30)
    msg     = models.TextField(max_length=200)
