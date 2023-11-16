from django.shortcuts import render
from .models import Post


# Create your views here.
def hompage(request):
    """
    function for rendering posts on homepage
    """
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, "blog/index.html", context)