from django.db import models

# Create your models here.
class TableOfMonth(models.Model):

    author = models.CharField(max_length=20)
    confirm = models.CharField(max_length=20, blank=True)
    date = models.DateField()
    notes = models.TextField(blank=True, default='')
    # records
    # shifts

    def __str__(self):
        return '%s年%s月份輪值表' % (self.date.year, self.date.month)


class Shift(models.Model):

    date = models.DateField()
    man = models.CharField(max_length=20)
    substitute = models.CharField(max_length=20, blank=True)
    table = models.ForeignKey('TableOfMonth', related_name='shifts')

    def __str__(self):
        return '%s/%s/%s' % (self.date.year, self.date.month, self.date.day)
