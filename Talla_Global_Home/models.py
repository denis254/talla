from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

import datetime


from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone_Number = models.CharField(max_length=30, null = True)
    Cash_Invested = models.CharField(max_length=30, default = 0.00)
    Interest = models.CharField(max_length=30, default = 0.00)
    Investment_Date = models.DateTimeField('Investment Date', null = True)


    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
