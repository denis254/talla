from django.db import models

# Create your models here.

from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Point_Balance = models.CharField(max_length=30, default = 0.00)
    Cash_Balance = models.CharField(max_length=30, default = 0.00)
    User_Type = models.CharField(max_length = 100, choices=[('Free','Free'),('Starter','Starter'),('Business','Business'),('Professional','Professional')], default = 'Free')


    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
