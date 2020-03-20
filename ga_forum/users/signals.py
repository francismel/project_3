from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print('Hitting')
    print('created',created)
    print('sender',sender)
    print('instance',instance)
    print('kwargs',kwargs)
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)

def save_profile(sender, instance, **kwargs):
    print("hitting in save_profile")
    print('kwargs',kwargs)
    if kwargs['created']:
        instance.profile.save()