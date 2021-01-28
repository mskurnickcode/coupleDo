from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name ="index"),
    path("login", views.login_view, name = "login"),
    path("logout", views.logout_view, name = "logout"),
    path("register", views.register, name = "register"),
    path("post/<slug:post_slug>", views.post, name = "post"),
    path("category/<slug:category_slug>", views.category, name = "category"),

]