from django.shortcuts import get_object_or_404, render
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import markdown


def post(request, post_slug):
    """View for a specific post in the posts application.

    Args:
        request: HttpRequest object.
        post_slug: The slug of the requested post.
    """
    post = get_object_or_404(Post, slug=post_slug)
    context = dict()
    context["post"] = post
    context["content_html"] = markdown.markdown(post.content)
    return render(request, "posts/post.html", context)


def posts(request):
    """View for all posts in the posts application.

    Args:
        request: HttpRequest object.
    """
    context = dict()
    context["posts"] = Post.objects.order_by('title')
    return render(request, "posts/index.html", context)


@api_view(['GET'])
def post_detail(request, slug):
    """
    A view that returns post data (for a singular post) in JSON.

    Args:
        request: HttpRequest object.
        slug: The slug of the requested post.
    """
    post = get_object_or_404(Post, slug=slug)
    serializer = PostSerializer(post)
    return Response(serializer.data)


@api_view(['GET'])
def posts_list(request):
    """
    A view that returns post data (for all posts) in JSON.

    Args:
        request: HttpRequest object.
    """
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
