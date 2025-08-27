from django import forms

class BlogForm(forms.Form):
    author = forms.CharField(max_length=10)