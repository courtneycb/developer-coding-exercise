from django.shortcuts import get_object_or_404, render
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import markdown

# Feel free to move this to a new file if you are carrying out the 'tags' calculation there
stopWords = [
    "#", "##", "a", "about", "above", "after", "again", "against", "all", "am",
    "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
    "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
    "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
    "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
    "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
    "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that",
    "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
    "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
    "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
    "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where",
    "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
    "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves"
]

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
def posts_list(request):
    """
    A view that returns post data (for all posts) in JSON.

    Args:
        request: HttpRequest object.
    """
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
