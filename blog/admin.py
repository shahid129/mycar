from django.contrib import admin
from .models import PostAd, CustomerComment, Images
from django_summernote.admin import SummernoteModelAdmin

class ImagesAdmin(admin.StackedInline):
    model = Images
    
@admin.register(PostAd)
class PostAdAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('price', 'created_on', 'year')
    list_display = ('title', 'author', 'created_on', 'tax', 'nct')
    search_fields = ('title', 'content', 'year')
    summernote_fields = ('description')
    inlines = [ImagesAdmin]


@admin.register(CustomerComment)
class CustomerCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


