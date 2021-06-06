from django import forms
from django.forms import ModelForm
from .models import Comments

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={"rows": 10, "cols":80, "placeholder": "Leave your comment or ask a question if you have!"})}
