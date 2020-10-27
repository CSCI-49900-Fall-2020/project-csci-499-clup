from django.db import models

# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django import forms 

class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField() 

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=31, blank=True)
    cell_number = models.CharField(max_length=12, blank=False)

<<<<<<< HEAD
=======
#Customer Registration
class Customer(models.Model):
    user = models.OneToOneField(User, default="", on_delete=models.CASCADE)
    username = models.CharField(max_length=30, default="")
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=100, default="123@gmail.com")
    phone_number = models.CharField(max_length=12, default="")
    password1 =  models.CharField(max_length=30, default="")
    is_customer = models.BooleanField(default=True)
    is_business = models.BooleanField(default=False)

#business table
class Business(models.Model):
    username = models.CharField(max_length=30, default="")
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=100, default="123@gmail.com")
    phone_number = models.CharField(max_length=12, default="")
    store_name = models.CharField(max_length=100, default="")
    store_number = models.CharField(max_length=12, default="")
    store_address = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=30, default="New York")
    state = models.CharField(max_length=2, default="")
    zipcode = models.CharField(max_length=5, default="")
    input_sex = models.CharField(max_length=3, default="")
    is_customer = models.BooleanField(default=False)
    is_business = models.BooleanField(default=True)
    # business hours
    sunday_open = models.CharField(max_length=5, default="")
    sunday_closed = models.CharField(max_length=5, default="")
    monday_open = models.CharField(max_length=5, default="")
    monday_closed = models.CharField(max_length=5, default="")
    tuesday_open = models.CharField(max_length=5, default="")
    tuesday_closed = models.CharField(max_length=5, default="")
    wednesday_open = models.CharField(max_length=5, default="")
    wednesday_closed = models.CharField(max_length=5, default="")
    thursday_open = models.CharField(max_length=5, default="")
    thursday_closed = models.CharField(max_length=5, default="")
    friday_open = models.CharField(max_length=5, default="")
    friday_closed = models.CharField(max_length=5, default="")
    saturday_open = models.CharField(max_length=5, default="")
    saturday_closed = models.CharField(max_length=5, default="")

    def __iter__(self):
        return iter([self.username, self.first_name, self.last_name, self.email,
         self.phone_number, self.store_name, self.store_number,
         self.store_address, self.city, self.state, self.zipcode, 
         self.input_sex, self.is_customer, self.is_business])
    
>>>>>>> parent of 5b4016ae... Removed input sex
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

#business table
class business(models.Model):
    email = models.CharField(max_length=127, default='')
    first_name = models.CharField(max_length=127, default='')
    middle_name = models.CharField(max_length=127, default='')
    last_name = models.CharField(max_length=127, default='')
    password = models.CharField(max_length=127, default='')
    cellnumber = models.CharField(max_length=127, default='')
