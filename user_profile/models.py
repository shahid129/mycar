from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    """
    User can create a profile and update their profile with their details
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, unique=False, null=True)
    last_name = models.CharField(max_length=100, unique=False, null=True)
    email = models.EmailField(unique=True, null=True)
    date_of_birth = models.DateField(unique=False, null=True)
    phone = models.IntegerField(null=True)
    image = models.ImageField(null=True, default='/static/images/audi.jpeg')
    about_me = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
