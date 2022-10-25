from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Add different fields to admin
    """
    list_display = ('first_name', 'last_name', 'date_of_birth', 'phone')
    list_filter = ('first_name', 'last_name')
