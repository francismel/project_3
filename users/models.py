from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profile_pics/unknown.png',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)

        if img.height >250 or img.width >250:
            img_dimen = (250,250)
            img.thumbnail(img_dimen)
            img.save(self.profile_pic.path)


# class Event(models.Model):
#     host = models.OneToOneField(User, on_delete=models.CASCADE)
#     date = models.DateTimeField(default=timezone.now)
#     location = models.TextField()




# Create your models here.
