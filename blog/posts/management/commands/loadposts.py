import os
from django.core.management.base import BaseCommand
# from django.conf import settings
from posts.models import Post


class Command(BaseCommand):
    """Required command class for the custom Django loadposts command."""

    help = "Converts Markdown files listed under assets/posts and stores"

    def handle(self, *args, **options):
        PATH = os.path.abspath('../assets/posts')
        SEPARATOR = '==='

        # For every blog post markdown file
        for post_file in os.listdir(PATH):
            post_f = open(os.path.join(PATH, post_file), 'r')
            post_string = post_f.read()

            # Get the heading and content data
            file_content = post_string.strip(SEPARATOR).split(SEPARATOR)
            heading = file_content[0].strip('\n').split('\n') # An array of the title, author and slug
            
            title = heading[0].replace('Title: ', '')
            author = heading[1].replace('Author: ', '')
            slug = heading[2].replace('Slug: ', '')

            content = file_content[1] # The blog post content as a string
            
            # Create blog post object and save to the db
            post = Post(
                slug=slug.strip(),
                title=title.strip(),
                author=author.strip(),
                content=content.strip()
            )

            post.save()
            self.stdout.write('Blog post "{}" saved.'.format(title))
