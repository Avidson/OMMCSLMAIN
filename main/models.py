from django.db import models
import sys 
from django.db import models
from django.contrib.auth.models import User
from custom_code.utils import calculate_emi
import math
from django.shortcuts import reverse
from django.conf import settings


# Create your models here.

class Profile(models.Model):
    profile_owner = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, editable=False, default=0)
    first_name = models.CharField(max_length=150, default='your occupation', editable=False)
    last_name = models.CharField(max_length=150, default='your occupation', editable=False)
    occupation = models.CharField(max_length=150, default='your occupation', editable=False)
    state_residence = models.CharField(max_length=200, default='Home address', editable=False)
    home_address = models.CharField(max_length=200, default='address', editable=False)
    phone_number = models.CharField(max_length=200, default='0908987679', editable=False)
    email = models.CharField(max_length=200, default='example@email.com')
    registration_fee = models.FloatField(default=0, editable=False)
    payment_date = models.DateField(auto_now=True)
    paid = models.BooleanField(default=False)
    payment_ref = models.CharField(max_length=200, default='None', editable=False)
    passport = models.ImageField(default='None', upload_to='profilePassports/')

    def __str__(self):
        return self.home_address
    
    def get_registration_fee(self):
        return self.registration_fee
    
    def get_absolute_url(self):
        return reverse('main:youmade-payment_pdf', args=[self.pk])
    

class Dashboard(models.Model):
    pass 


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name





        



    

 

