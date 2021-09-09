from django import forms

class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField()
    hashtag = forms.CharField()
    image = forms.ImageField()

class CommentForm(forms.Form):
     text = forms.CharField()