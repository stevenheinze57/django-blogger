from django.urls import path
from . import views

app_name = 'blogger'
urlpatterns = [
    path('', views.BloggerView.as_view(), name='index'),
]
