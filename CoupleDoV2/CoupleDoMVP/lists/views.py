from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError, models
from django.db.models import F, Count
from django.urls import reverse
from markdown2 import markdown
from .models import *
from .helpers import *

# Create your views here.
def index(request):
    most_read_posts = Post.objects.order_by('blog_views')[:3]
    latest_posts = Post.objects.order_by('date')[:5]
    return render(request, "lists/index2.html", {
        "most_read_posts": most_read_posts,
        "latest_posts": latest_posts,
        })


def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "lists/login2.html", {
                "message": "Invalid Credentials"
            })
    else:
        return render(request, "lists/login2.html")


def logout_view(request):
    logout(request)
    return render(request, "lists/login.html", {
                "message": "Logged Out"
            })


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "lists/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "lists/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "lists/register.html")

def category(request, category_slug):
    category = Category.objects.get(category_slug = category_slug)
    posts = Post.objects.filter(category=category)
    print(posts)
    return render(request, 'lists/categories.html', {
        "category": category,
        "posts": posts,
    })



def post(request, post_slug):
    if post_slug:
        try: 
            post = Post.objects.get(post_slug = post_slug)
            Post.objects.filter(post_slug= post_slug).update(blog_views=F('blog_views') + 1)
            post.body = markdown(post.body)
            return render(request, "lists/post2-right-template.html", {
                "post" : post
            })
        except:
            return render(request, "lists/no-sidebar-template.html", {
                "message": "The page you requested could not be found.  Please try another page or use the contact us to let us know."
            })  
    else:
        return render(request, "lists/no-sidebar-template.html", {
            "message": "The page you requested could not be found.  Please try another page or use the contact us to let us know."
        })
