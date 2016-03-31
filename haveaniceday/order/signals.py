from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from order.models import Member

@receiver(post_save, sender=Member)
def model_post_save(sender, **kwargs):
    print('test')
    if kwargs['created'] is True:
        print('Created: {}'.format(kwargs['instance'].__dict__))
    else:
        print('Updated: {}'.format(kwargs['instance'].__dict__))
