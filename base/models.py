from django.db import models
from django.contrib.auth.models import User
# Create your models here.

ROLES = (
   ('Admin', 'Admin - Can Delete Members'),
   ('Regular', 'Regular- Cannot Delete Members')
)

class Team(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(max_length = 254,null=True, blank=True)
    phone_number = models.CharField(max_length=12,null=True, blank=True)
    # description = models.TextField(null=True, blank=True)
    # complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    role = models.CharField(choices=ROLES, max_length=128, default='Regular')


    def __str__(self):
        return self.title

    
    class Meta:
        ordering = ['create']
