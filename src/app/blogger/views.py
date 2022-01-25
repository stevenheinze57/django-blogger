from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import BlogPost

# Create your views here.

class BloggerView(generic.TemplateView):
    template_name = 'blogger/index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['blog_posts'] = BlogPost.objects.all()
        return context
