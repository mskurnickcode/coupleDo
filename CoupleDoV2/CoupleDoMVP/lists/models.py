from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
import uuid

# Create your models here.

class User(AbstractUser):
    pass

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    tag_slug = models.SlugField(max_length=100, unique=True, default='')
    author = models.ForeignKey(User, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category_slug = models.SlugField(max_length=100, unique=True)
    category_description = models.TextField(default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    authorID = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default='', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    post_slug = models.SlugField(max_length=100, unique=True, default=uuid.uuid1)
    imageURL = models.URLField(max_length = 200, default='')
    blog_views=models.IntegerField(default=0)

    def __str__(self):
        return self.title
