import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings


MEMBERSHIP_CHOICES = (
    ('Free', 'free'),
    ('VIP', 'vip'),
)
 

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    displayingContactInfo = models.BooleanField(default=True)
    phoneNo = models.CharField(max_length=20, null=True)

    def __str__(self):
        return ('profil de utilizator ' + self.user.username)

    class Meta:
        verbose_name = "Profil de utilizator (User Profiles)"
        verbose_name_plural = "Profile de utilizator (User Profiles)"


class Membership(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    isPaymentStatusActive = models.BooleanField(default=True)

    date = models.DateField(("Date"), default=datetime.date.today)


    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES, 
        max_length=30,
        default='Free',
        )
    
    def __str__(self):
        return ('Abonamentul lui ' + self.user.username)

    class Meta:
        verbose_name = "Abonament (membership)"
        verbose_name_plural = "Abonamente (memberships)"



def after_creating_an_user(sender, instance, created, *args, **kwargs):
    if created:
        print('created post_save 8hfg2o3gpefh3go2fjwurygt3984fhibwi  ' , instance)
        newMembership = Membership()
        newMembership.user = instance
        newMembership.save()

        newUserProfile = UserProfile()
        newUserProfile.user = instance
        newUserProfile.save()
post_save.connect(after_creating_an_user, sender=User)


