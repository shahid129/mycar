from django.db import models
from blog.models import PostAd


# Create your models here.
class UserProfile(models.Model):
    """
    User can create a profile and update their profile with their details
    """
    first_name = models.CharField(max_length=100, unique=False)
    last_name = models.CharField(max_length=100, unique=False)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(unique=False)
    phone = models.IntegerField()
    image = models.ImageField()
    about_me = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name
