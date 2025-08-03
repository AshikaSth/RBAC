import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    ROLE_CHOICES= (
        ('teacher', 'Teacher'),
        ('Student','student',) 

    )
    role= models.CharField(max_length= 10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.username
    
    