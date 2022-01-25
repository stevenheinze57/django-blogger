from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=3000)
    date_time = models.DateTimeField()
