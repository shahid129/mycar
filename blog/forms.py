from django import forms
from .models import PostAd
import django_filters


class PostForm(forms.ModelForm):

    class Meta:
        model = PostAd
        fields = ('title', 'price', 'image', 'year', 'nct', 'tax', 'description',)

