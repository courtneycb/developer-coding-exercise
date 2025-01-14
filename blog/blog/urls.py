"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from posts.views import posts
from posts import views

app_name = "blog"
urlpatterns = [
    path(r'', posts, name='home'),
    path(r'admin/', admin.site.urls),
    path(r'posts/', include('posts.urls')),
    path(r'posts-list', views.posts_list, name='posts-list'),
    path(r'post-detail/<slug:slug>', views.post_detail, name='post-detail')
]
