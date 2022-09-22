from django import forms
from django.forms import ModelForm
from . models import UserProfile


class UserProfileForms(forms.ModelForm):
    """
    Creates user profile form
    """
    class Meta:
        model = UserProfile
        fields = '__all__'
