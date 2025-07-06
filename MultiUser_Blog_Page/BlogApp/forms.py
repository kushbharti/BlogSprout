from django import forms
from .models import Blogpost

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title','content','images']
        widgets = {
            'title' :forms.TextInput(attrs={'name':'title' ,'placeholder':'Enter the Title.'}),
            'content' :forms.Textarea(attrs={'name':'content' ,'placeholder':'Content of the Post.','rows':2}),
            'images':forms.ClearableFileInput(),
        }