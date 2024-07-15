from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from golf.manager import CustomUserManager
from django.contrib.auth.models import Group, Permission
# Create your models here.


class Events(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField()
    location = models.CharField(max_length= 200)
    ticket_price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    date = models.DateField(auto_now = False, auto_now_add = False,)

    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title
    

class Person(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length= 20)
    profession = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    

    

class Member(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    comments = models.TextField()

    def __str__(self):
        return self.email
    


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique = True)
    first_name = models.CharField(max_length = 40, blank = True)
    last_name = models.CharField(max_length = 40, blank = True)
    is_staff = models.BooleanField(default = True)
    is_active = models.BooleanField(default = True)
    date_joined = models.DateTimeField(auto_now_add= True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = []
  
    