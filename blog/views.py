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

def post_detail(request, post_id):
    """
    function for getting and displaying a specific post
    """
    post = Post.objects.get(pk=post_id)
    context = {
        'post':post,
    }
    return render(request, "blog/post-detail.html" , context )