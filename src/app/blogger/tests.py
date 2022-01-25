from django.test import TestCase
from .models import BlogPost
import datetime

# Create your tests here.
class BloggerPageViewTest(TestCase):
    def test_get_blogger_page(self):
        response_blogger = self.client.get('https://localhost:8000/blogger/')
        self.assertEqual(response_blogger.status_code, 200)


class BlogPostModelTest(TestCase):
    def test_create_blog_post(self):
        test_blog_post = BlogPost.objects.create(title="Test Blog Post", content="My blog content", date_time=datetime.datetime.now())
        test_blog_post.save()
        self.assertEqual(test_blog_post.__class__.__name__, BlogPost.__name__)
        self.assertIsNotNone(test_blog_post)
