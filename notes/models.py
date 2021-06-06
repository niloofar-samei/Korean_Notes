from django.db import models
import datetime
from django.utils import timezone

class Notes(models.Model):
    title = models.CharField(max_length=100)
    quick_note = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.quick_note

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(deys=1)

class Comments(models.Model):
    note = models.ForeignKey(Notes, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
