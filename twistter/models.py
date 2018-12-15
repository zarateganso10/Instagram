from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class PostText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.text


class Profile(models.Model):
    friends = models.ManyToManyField(User, related_name='friends')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    biografia = models.TextField(blank=True, null=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
   if created:
       Profile.objects.create(user=instance)
   instance.profile.save()