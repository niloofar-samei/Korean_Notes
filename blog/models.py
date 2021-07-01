from django.db import models
import datetime
from django.utils import timezone

class Note(models.Model):
    title = models.CharField(max_length=100)
    quick_note = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=100)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.quick_note

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(deys=1)

class Comment(models.Model):
    text = models.CharField(max_length=200)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
