"""Serializers for posts models."""

from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for blog posts."""

    url = serializers.HyperlinkedIdentityField(
        view_name='post-detail',
        lookup_field='slug'
    )

    class Meta:
        """Meta settings for serializer."""

        model = Post
        fields = (
            'title',
            'author',
            'content',
            'tags',
            'url'
        )
