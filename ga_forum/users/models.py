from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profile_pics/unknown.png',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


# class Event(models.Model):
#     host = models.OneToOneField(User, on_delete=models.CASCADE)
#     date = models.DateTimeField(default=timezone.now)
#     location = models.TextField()




# Create your models here.
