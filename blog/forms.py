from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import PostAd, CustomerComment


class DateInput(forms.DateInput):
    """
    Generate date picker for the form
    """
    input_type = 'date'
    

class PostForm(forms.ModelForm):

    class Meta:
        model = PostAd
        fields = ('title', 'price', 'image', 'year', 'nct', 'tax', 'description',)
        widgets = {
            'year': DateInput(),
            'nct': DateInput(),
            'tax': DateInput(),
        }


# Create user log in form

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # Add custom help text
    # help was taken from 
    # https://stackoverflow.com/questions/56464571/how-to-disable-django-registration-password-help-text

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)    
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomerCommentForm(forms.ModelForm):
    class Meta:
        model = CustomerComment
        fields = ('body',)