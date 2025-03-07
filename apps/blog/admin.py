from uuid import uuid4
from django.contrib import admin
from .models import Post, Comment, PostView, Like
# Register your models here.


class PostAdminManager(admin.ModelAdmin):
    list_display = ['title', 'author']
    search_fields = ['title', 'content']
    list_filter = ['author']
    list_per_page = 10
    prepopulated_fields = {'slug': ('title',)}
    uneditable_fields = ['slug']


admin.site.register(Post, PostAdminManager)

admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Like)
