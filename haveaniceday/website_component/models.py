from django.db import models

# Create your models here.
class CustomWebPage(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CustomComponent(models.Model):

    name = models.CharField(max_length=20)
    value = models.CharField(max_length=100, blank=True)
    page = models.ForeignKey('CustomWebPage', related_name='components')

    def __str__(self):
        return '%s:%s(%s)' % (self.page ,self.name, self.value)
