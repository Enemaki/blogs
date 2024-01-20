from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    """This represents an overall blog"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return a string representation of a model"""
        return self.text
    
class Tweet(models.Model):
    """This represents an individual blog post"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def meta(self):
        verbose_name_plural = 'tweets'
    def __str__(self):
        """Return a string representation of a model"""
        return f"{self.text[:50]}..."