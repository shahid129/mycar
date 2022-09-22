from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import UserProfile
from .forms import UserProfileForms

# Create your views here.

# class UserProfilePage(ListView):
#     """
#     Users can create a profile
#     """

# model = UserProfile
# fields = ('__all__')
# template_name = 'user_profile/index.html'


def user_profile_page(request):
    items = UserProfile.objects.all()
    context = {
        'items': items
    }
    return render(request, 'user_profile/index.html', context)
