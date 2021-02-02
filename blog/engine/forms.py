from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Class of form for comments.
    Provides 'text' field of Comment model for input.
    """

    class Meta:
        model = Comment
        fields = ('text', )
