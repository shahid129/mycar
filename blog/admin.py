from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PostAd, CustomerComment, Images


class ImagesAdmin(admin.StackedInline):
    """
    Users can add multiple images
    """
    model = Images


@admin.register(PostAd)
class PostAdAdmin(SummernoteModelAdmin):
    """
    Add Different fields to admin
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('price', 'created_on', 'year')
    list_display = ('title', 'author', 'created_on', 'tax', 'nct')
    search_fields = ('title', 'content', 'year')
    summernote_fields = ('description')
    inlines = [ImagesAdmin]


@admin.register(CustomerComment)
class CustomerCommentAdmin(admin.ModelAdmin):
    """
    Admin can approve customer comments
    """
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
