from django.db import models
import requests

class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete = models.CASCADE,)
    body = models.TextField()
    tag = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    
