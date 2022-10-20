from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.forms import ModelForm
from .models import PostAd, CustomerComment, Images


class PostForm(forms.ModelForm):
    """
    Create a form where user can upload the detail of the car
    """

    # Add CSS class to the field
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'register_form',
                'placeholder': 'Car Name'
                }
            ),
        label=''
    )

    # Add CSS class to the field
    price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'register_form',
                'placeholder': 'Price in Euro'
                }
            ),
        label=''
    )

    # Add CSS class and attr to the field
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'register_form',
                'placeholder': 'Details about car',
                'style': 'height: 10em;'
                }
            ),
        label=''
    )

    # Add CSS class and attr to the field
    year = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'register_form', 
                'placeholder': 'Model Year',
                'type': 'date'
                }
            ),
        label='Model Year'
    )

    # Add CSS class and attr to the field
    nct = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'register_form',
                'placeholder': 'NCT Expiry',
                'type': 'date'
                }
            ),
        label='NCT Expiry'
    )

    # Add CSS class and attr to the field
    tax = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'register_form',
                'placeholder': 'Tax Expiry',
                'type': 'date'
                }
            ),
        label='Tax Expiry'
    )

    # Add CSS class and attr to the field
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control register_form',
                'id': 'customFile'
                }
            ),
        label=''
    )

    class Meta:
        """
        Thesse are the available fields for postform
        """
        model = PostAd
        fields = (
            'title',
            'price',
            'image',
            'year',
            'nct',
            'tax',
            'description',
        )

    # Remove image label
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = ''


# Create user log in form
class NewUserForm(UserCreationForm):
    """
    Create a login form
    """
    email = forms.EmailField(required=True)

    class Meta:
        """
        Available fields for the login form
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    # Add CSS class and attr to the field
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'register_form',
                'placeholder': 'User Name'
                }
            ),
        label=''
    )

    # Add CSS class and attr to the field
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'register_form',
                'placeholder': 'Email'
                }
            ),
        label=''
    )

    # Add CSS class and attr to the field
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'register_form',
                'placeholder': 'Password'
                }
            ), 
        label=''
    )

    # Add CSS class and attr to the field
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'register_form',
                'placeholder': 'Confirm'
                }
            ),
        label=''
    )

    # Add custom help text
    # help was taken from 
    # https://stackoverflow.com/questions/56464571/how-to-disable-django-registration-password-help-text
    def __init__(self, *args, **kwargs):
        """
        A function to remove the help text from the form
        """
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
    """
    Create a customer comment form
    """
    class Meta:
        """
        Available fields for customer comment form
        """
        model = CustomerComment
        fields = ('body',)


class ImagesForm(forms.ModelForm):
    """
    User can add multiple images
    """

    # Add CSS class and attr to the field
    images = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control register_form',
                'id': 'customFile'
                }
            )
        )

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
