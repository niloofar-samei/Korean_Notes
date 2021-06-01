from django.db import models
import datetime
from django.utils import timezone

class Notes(models.Model):
    note_title = models.CharField(max_length=100)
    note_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.note_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(deys=1)

class Comments(models.Model):
    note = models.ForeignKey(Notes, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
