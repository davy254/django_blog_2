from django.db import models
from django.urls import reverse
from  django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Category(models.Model):
    """
    Model for defining blog category attributes
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model for defining blog post attribites
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    blog_image = models.ImageField(default='new_post.jpg', upload_to='blog_pics', verbose_name='blog-image')
    
    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk':self.pk})

    
    