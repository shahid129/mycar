from django.contrib import admin
from .models import UserProfile


# Register your models here.
# admin.site.register(UserProfile)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'phone')
    list_filter = ('first_name', 'last_name')
    search_fields = ('phone', 'first_name', 'last_name')
