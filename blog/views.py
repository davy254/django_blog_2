from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import CreateView
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

def post_detail(request, pk):
    """
    function for getting and displaying a specific post
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return render(request, "blog/404.html")
    context = {
        'post':post,
    }
    return render(request, "blog/post-detail.html" , context )


class PostCreateView(CreateView):
    model = Post
    fields = ['title','content', 'slug','categories', 'blog_image']
    template_name = "blog/post-create.html"

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
