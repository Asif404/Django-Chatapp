from django.db import models
from django.contrib.auth.models import User

class Rooms(models.Model):
    name =models.CharField(max_length=255)
    slug =models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Rooms,related_name='message',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='message',on_delete=models.CASCADE)
    content = models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
# Create your models here.
