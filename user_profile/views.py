from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForms


def user_profile_page(request):
    """
    User profile page
    """
    profile = UserProfile.objects.filter(user=request.user)[0]

    context = {
        'profile': profile
    }
    return render(request, 'user_profile/profile.html', context)


def edit_user_profile(request, username):
    """
    User can edit and update their profile
    """
    profile_list = UserProfile.objects.filter(user=request.user)
    if request.method == 'POST':
        if len(profile_list) > 0:
            profile = profile_list[0]
            form = UserProfileForms(request.POST, request.FILES,
                                    instance=profile)
        else:
            form = UserProfileForms(
                request.POST, request.FILES, instance=request.user.id)

        if form.is_valid():
            form.save()
            messages.info(request, 'Profile updated successfully.')
            return redirect('user_profile')

    if len(profile_list) > 0:
        profile = profile_list[0]
        form = UserProfileForms(instance=profile)
    else:
        form = UserProfileForms(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'user_profile/edit_profile.html', context)
