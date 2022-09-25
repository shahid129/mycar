from django.shortcuts import render, get_object_or_404, redirect, reverse
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
            form = UserProfileForms(request.POST, request.FILES, instance=request.user.id)
        print('pre save')
        if form.is_valid():
            print('valid')  # Check if form is valid
            form.save()
            return redirect('user_profile')
        else:
            print('not posting')
    if len(profile_list) > 0:
        profile = profile_list[0]
        form = UserProfileForms(instance=profile)
    else:
        form = UserProfileForms(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'user_profile/edit_profile.html', context)
