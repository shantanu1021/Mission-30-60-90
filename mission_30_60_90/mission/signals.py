from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Missions, Status


@receiver(post_save,sender=Missions)
def create_status(sender, instance, created, **kwargs):
    if created:
        for i in range(instance.no_of_days):
            Status.objects.create(mission_id = instance,day_no=i+1,is_done=False,remarks="")
        #Profile.objects.create(user=instance)

'''
@receiver(post_save,sender=Missions)
def save_status(sender, instance, **kwargs):
    instance.status.save()
'''

