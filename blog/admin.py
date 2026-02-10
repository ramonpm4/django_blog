from django.contrib import admin

# Register your models here.

from .models import Author, Post, Tag

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Author, BookAdmin)
admin.site.register(Post)
admin.site.register(Tag)