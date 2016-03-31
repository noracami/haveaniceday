from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from order.models import Member

@receiver(pre_save, sender=Member)
def model_pre_save(sender, **kwargs):
    print('another test')
    kwargs['instance'].splitlocation()
