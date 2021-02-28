from django.db import models

# Create your models here.

# ‘event_name’, ’data’, ’time’, ‘location’, ’image’, ‘is_liked’
from django.conf import settings

# import datetime

class Model_Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    event_name = models.CharField(max_length=20)
    data=models.TextField()
    time = models.CharField(max_length=76)
    location=models.CharField(max_length=30)
    image = models.ImageField(upload_to="media/", blank=True)
    objects = models.Manager()
    is_liked = models.ManyToManyField( settings.AUTH_USER_MODEL, related_name="user_likes")
    def count_likes(self):
        return self.is_liked.count()

    def check_like(self, user23):
        return self.is_liked.filter(id=user23.id).exists()

    def __unicode__(self):
        return self.id
