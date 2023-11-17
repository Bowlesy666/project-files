from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('approved', 'created_on')
    list_display = ('user_name', 'body', 'post', 'created_on', 'approved')
    search_fields = ['user_name', 'body']
    actions = ['approve_comments']

    # Comments should be auto approved,
    # function here is to review and remove posts that violate standards
    def approve_comments(self, request, queryset):
        queryset.update(approved=False)
