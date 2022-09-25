from django import forms
from django.forms import ModelForm
from . models import UserProfile


class UserProfileForms(forms.ModelForm):
    """
    Creates user profile form
    """
    class Meta:
        model = UserProfile
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'phone', 'image', 'about_me', ]
