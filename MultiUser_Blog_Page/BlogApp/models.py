from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blogpost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    images = models.ImageField(upload_to='pictures/',blank=True,null=True)
    created_day = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    