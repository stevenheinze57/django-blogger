from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.ContactFormView.as_view()),
    path('index', views.ContactFormView.as_view(), name='index'),
    path('successful', views.get_successful_page, name='successful'),
    path('unsuccessful', views.get_unsuccessful_page, name='unsuccessful'),
]
