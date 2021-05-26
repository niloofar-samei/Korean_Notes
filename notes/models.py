from django.db import models

class notes(models.Model):
    note_title = models.CharField(max_length=100)
    note_text = models.CharField(max_length=500)
    pud_date = models.DateTimeField('date published')
    author = models.CharField(max_length=100)
