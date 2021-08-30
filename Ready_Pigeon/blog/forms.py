from .models import Comment, Post
from django import forms


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body':forms.Textarea(attrs={'class': 'form-control','style': 'width:100%'}),
            
        }
