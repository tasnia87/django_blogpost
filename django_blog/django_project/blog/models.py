from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField()
    niche=models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


# Create your models here.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.TextField()


    def __str__(self):
        return self.name