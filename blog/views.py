from django.http import Http404
from django.shortcuts import redirect, render
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.db.models import  Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Post


# Create your views here.
# def hompage(request):
#     """
#     function for rendering posts on homepage
#     """
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 5)
#     page_number = request.GET.get('page')
#     print(request.GET.get('page'))
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'posts':posts,
#         'page_obj': page_obj
#     }
#     return render(request, "blog/index.html", context)
class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-pub_date']
    paginate_by = 4


def post_detail(request, slug):
    """
    function for getting and displaying a specific post
    """
    try:
        post = Post.objects.get(slug=slug)
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
    fields = ['title','content','categories', 'blog_image']
    template_name = "blog/post-create.html"

    def form_valid(self,form):
        form.instance.author = self.request.user
        try:
            print("saving post.....")
            if not form.instance.slug:
                form.instance.slug = slugify(form.instance.title)
            print("slug", form.instance.slug)
        except Exception as e:
            print(f'Error saving post:  {e}')
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    """
    class based generic view for updating posts
    """
    model = Post
    fields = ['title','content', 'categories', 'blog_image']
    template_name = "blog/post-create.html"


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'


def search(request):
    """
    Function for searching blog post via title or content
    """
    search_query = request.GET.get('search', '')
    print(search_query)

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
        if posts:
            return render(request, 'blog/search_results.html', {'posts': posts})
        else:
            return render(request, 'blog/no_search_results.html')

    else:
        return redirect('blog:homepage')

