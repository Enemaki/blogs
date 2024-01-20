from django import forms

from .models import Blog, Tweet

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['text']
        labels = {'text': ''}
        
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}