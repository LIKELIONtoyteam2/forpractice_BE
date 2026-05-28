from django.contrib import admin

# Register your models here.
from .models import Post, Hashtag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    filter_horizontal = ['hashtag'] 

admin.site.register(Hashtag)