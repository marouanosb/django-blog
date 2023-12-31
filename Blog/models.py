from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title =  models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(default=timezone.now) #  (auto_now=True) => updates everytime it is modified / (auto_now_add=True) => when created but can't be changed
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #to show the title in the result query
    def __str__(self):
        return self.title