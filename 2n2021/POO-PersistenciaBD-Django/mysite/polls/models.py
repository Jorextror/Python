import datetime
from turtle import title
# Username: admin
# Email address: admin@example.com
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    valoration=[1,2,3,4,5]
    
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Valoration(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text