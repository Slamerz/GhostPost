from django.db import models
import datetime
from django.utils import timezone


class Post(models.Model):
    isBoast = models.BooleanField(default=True)
    content = models.CharField(max_length=280)
    upVotes = models.IntegerField(default=0)
    downVotes = models.IntegerField(default=0)
    dateSubmitted = models.DateTimeField('datePublished', default=timezone.now())
    secretKey = models.CharField(max_length=6, default="666666")

    def __str__(self):
        return self.content

    def was_published_recently(self):
        return self.dateSubmitted >= timezone.now() - datetime.timedelta(days=1)

