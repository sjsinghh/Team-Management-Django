from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

ROLES = (
   ('Admin', 'Admin - Can Delete Members'),
   ('Regular', 'Regular- Cannot Delete Members')
)

class Team(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(max_length = 254,null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits are allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, null=True,blank=True) # validators should be a list
    create = models.DateTimeField(auto_now_add=True)
    role = models.CharField(choices=ROLES, max_length=128, default='Regular')


    def __str__(self):
        return self.title

    
    class Meta:
        ordering = ['create']
