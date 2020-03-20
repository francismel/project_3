from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    strContent = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author} said: {self.strContent} on {self.date}'

