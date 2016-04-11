from django.db import models

# Create your models here.
class Member(models.Model):
    class Meta:
        verbose_name = "人員"
    kmID = models.CharField(max_length=8, blank=True)
    edocID = models.CharField(max_length=20, blank=True)
    emailID = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=20)
    birthdate = models.DateField(blank=True, null=True)
    personalID = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=60, blank=True)
    location1 = models.CharField(max_length=20, blank=True, editable=False)
    location2 = models.CharField(max_length=20, blank=True, editable=False)
    location3 = models.CharField(max_length=20, blank=True, editable=False)
    title = models.CharField(max_length=20, blank=True)
    lastchangetime = models.DateTimeField('上次修改時間', auto_now=True, editable=False)
    notes = models.TextField(blank=True, default='')

    def splitlocation(self):
        locations = [x for x in self.location.split('-')]
        while len(locations) < 3:
            locations += ['']
        self.location1, self.location2, self.location3 = locations
        output = 'ori:%s -> [%s, %s, %s]' % (
            self.location, self.location1, self.location2, self.location3)
        print(output)
        return

    def __str__(self):
        resp = self.name
        f = lambda str: ('-(%s)' % str) if str!='' else ''
        resp += f(self.kmID)
        return resp
