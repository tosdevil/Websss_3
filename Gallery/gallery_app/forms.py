from .models import Comment
from django.forms import ModelForm, TextInput

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['author','comment_text']

        widgets = {
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "comment_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите свой комментарий'
            })
        }