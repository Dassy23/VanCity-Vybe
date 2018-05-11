from django.db import models
import requests

class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete = models.CASCADE,)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title
