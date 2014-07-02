"""
This will be your unit tests for the simple blog


"""

from django.test import TestCase

from models import Post

class SimplePostTest(TestCase):
    def setUp(self):
        # Create a 'Post' object
        blog_post = Post.objects.create(
                title = 'My test title',
                content = 'This is the blog content',
            )

    def test_post_save(self):
        """
        Test that post gets saved properly

        """
        post = Post.objects.get(
                title='My test title',
                content='This is the blog content'
            )
        self.assertEqual(post.title, 'My test title')
        self.assertEqual(post.content, 'This is the blog content')
