from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # django user table feilds all
    rolechoice = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    )
    role = models.CharField(max_length=20, choices=rolechoice, null=True, blank=True)