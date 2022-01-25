from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from .forms import ContactForm

# Create your views here.

def get_successful_page(request):
    template = loader.get_template('contact/successful.html')
    return HttpResponse(template.render())


def get_unsuccessful_page(request):
    template = loader.get_template('contact/unsuccessful.html')
    return HttpResponse(template.render())


class ContactFormView(generic.FormView):
    template_name = 'contact/index.html'
    form_class = ContactForm
    success_url = '/contact/successful'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)
