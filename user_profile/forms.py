from django import forms
from django.forms import ModelForm
from . models import UserProfile


class UserProfileForms(forms.ModelForm):
    """
    Creates user profile form
    """
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), label='')
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label='')
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Date of birth', 'type': 'date'}), label='')
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}), label='')
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'id': 'customFile'}), label='')
    about_me = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'About me', 'style': 'height: 10em;'}), label='')

    # image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'customFile'}), label='')
    class Meta:
        model = UserProfile
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'phone', 'image', 'about_me', ]
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForms, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'register_form form-control'