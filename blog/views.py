from django.shortcuts import render
from .models import Post
from django.views.generic  import ListView, DetailView
# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 1

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
def post(request, id):
    post = Post.objects.get(id=id)
    return render(request,'blog/post.html',{'post':post})