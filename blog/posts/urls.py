from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('', views.posts, name='posts'),
    path('<slug:post_slug>/', views.post, name='post'),
]
