from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(label="Leave your comment or ask a question if you have!", widget=forms.Textarea(attrs={"rows":10, "cols":80}))
