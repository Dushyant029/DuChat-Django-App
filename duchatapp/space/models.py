# Author: K. Dushyant Reddy
# StudID: STU614f75ed0b64d1632597485
# Social: https://www.linkedin.com/in/kdushyantreddy, https://github.com/Dushyant029 

from django.contrib.auth.models import User
from django.db import models

class Space(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

class Message(models.Model):
    space = models.ForeignKey(Space, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)