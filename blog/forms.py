from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import PostAd, CustomerComment, Images


class DateInput(forms.DateInput):
    """
    Generate date picker for the form
    """
    input_type = 'date'
    

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Car Name'}))                
    price = forms.CharField(widget=forms.TextInput(attrs={'class': 'title', 'placeholder': 'Price in Euro'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'title', 'placeholder': 'Details about car'}))
    # year = forms.DateField(widget=forms.TextInput(attrs={'class': 'date', 'placeholder': 'Model Year'}))
    # nct = forms.DateField(widget=forms.TextInput(attrs={'class': 'date', 'placeholder': 'NCT Expiry'}))
    # tax = forms.DateField(widget=forms.TextInput(attrs={'class': 'date', 'placeholder': 'Tax Expiry'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'customFile'}))
    

    class Meta:
        model = PostAd
        fields = ('title', 'price', 'image', 'year', 'nct', 'tax', 'description',)
        widgets = {
            'year': DateInput(attrs={'class': 'title', 'placeholder': 'heda'}),
            'nct': DateInput(attrs={'class': 'title'}),
            'tax': DateInput(attrs={'class': 'title'}),
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


class ImagesForm(forms.ModelForm):
    """
    User can add multiple images
    """
    images = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'customFile'}))

    class Meta:
        """
        Only images field is rendered to the page
        """
        model = Images
        fields = ('images',)