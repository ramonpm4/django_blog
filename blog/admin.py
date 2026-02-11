from django.contrib import admin

# Register your models here.

from .models import Author, Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tag', 'date_created',)
    list_display = ('title', 'date_created', 'author',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
