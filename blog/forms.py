from django import forms
from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={"placeholder": "Leave your comment or ask a question if you have!", "class": "comment-textarea textarea has-fixed-size", "id": "comment-textarea", "rows": 5})}
