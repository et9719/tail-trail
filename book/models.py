''' Imports '''
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Profile(models.Model):
    ''' define all infromation needed for users profile '''
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user", unique=True)
    owner = models.CharField(max_length=200)
    dog = models.CharField(max_length=50)
    address = models.TextField()
    phonenumber = PhoneNumberField(blank=True)
    info = models.TextField()


class Availability(models.Model):
    ''' Define what we need to know for the availability '''
    date = models.DateField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    requested = models.BooleanField(default=False)
    # requested by ?
    approved = models.BooleanField(default=False)

    class Meta:
        ''' Show availability in a list orded by date '''
        ordering = ['date']

    def __str__(self):
        return f"{self.date} {self.time}"
