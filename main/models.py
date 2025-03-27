from django.db import models
from django.conf import settings


class Category(models.Model):
    category = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.category

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_data = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='posts')

    def __str__(self):
        return self.title