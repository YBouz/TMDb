from django import forms
from .models import TitleReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = TitleReview
        # for testing purposes
        fields = ['author', 'title', 'rating', 'content']
        # fields = ['rating', 'content']
