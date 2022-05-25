from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
            return self.title
    
class Valoration(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    valoration=models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.valoration
    
