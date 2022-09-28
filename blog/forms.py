from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import PostAd, CustomerComment, Images


# class DateInput(forms.DateInput):
#     """
#     Generate date picker for the form
#     """
#     input_type = 'date'
    

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'register_form', 'placeholder': 'Car Name'}), label='')                
    price = forms.CharField(widget=forms.TextInput(attrs={'class': 'register_form', 'placeholder': 'Price in Euro'}), label='')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'register_form', 'placeholder': 'Details about car', 'style': 'height: 10em;'}), label='')
    year = forms.DateField(widget=forms.TextInput(attrs={'class': 'register_form', 'placeholder': 'Model Year', 'type': 'date'}), label='Model Year')
    nct = forms.DateField(widget=forms.TextInput(attrs={'class': 'register_form', 'placeholder': 'NCT Expiry', 'type': 'date'}), label='NCT Expiry')
    tax = forms.DateField(widget=forms.TextInput(attrs={'class': 'register_form', 'placeholder': 'Tax Expiry', 'type': 'date'}), label='Tax Expiry')
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control register_form', 'id': 'customFile'}), label='')
    

    class Meta:
        model = PostAd
        fields = ('title', 'price', 'image', 'year', 'nct', 'tax', 'description',)
        # widgets = {
        #     'year': DateInput(attrs={'class': 'register_form'}),
        #     'nct': DateInput(attrs={'class': 'register_form'}),
        #     'tax': DateInput(attrs={'class': 'register_form'}),
        # }

    # Remove image label
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = ''

# Create user log in form
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'register_form', 'placeholder': 'User Name'}), label='')
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'register_form', 'placeholder': 'Email'}), label='')
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'register_form', 'placeholder': 'Password'}), label='')
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'register_form', 'placeholder': 'Confirm'}), label='')

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
    images = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control register_form', 'id': 'customFile'}))

    class Meta:
        """
        Only images field is rendered to the page
        """
        model = Images
        fields = ('images',)
    
    # Remove images label
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].label = ''