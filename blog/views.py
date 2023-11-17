from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    """
    class based generic view for creating new posts
    """
    model = Post
    fields = ['title','content', 'slug','categories', 'blog_image']
    template_name = "blog/post-create.html"

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    """
    class based generic view for updating posts
    """
    model = Post
    fields = ['title','content', 'slug','categories', 'blog_image']
    template_name = "blog/post-create.html"


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

