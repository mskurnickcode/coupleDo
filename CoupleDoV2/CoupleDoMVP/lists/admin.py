from django.contrib import admin
from .models import Tag, User, Post, Category

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Category)