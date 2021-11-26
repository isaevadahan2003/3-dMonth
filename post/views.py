from typing import List
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import BlogPost, Comment

def hello_world_view(request):
    return HttpResponse('Hello, World!')

def date_view(request):
    now = datetime.now()
    return HttpResponse(str(now))

def blog_view(request):
    post: list = BlogPost.objects.all()
    return render(request, "blog.html", context={'posts': post})\

class PostDetailView(DetailView):
    queryset = BlogPost.objects.all()
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context: dict = super(PostDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        comments: List[Comment] = Comment.objects.filter(post_id=pk)
        context["comments"] = comments
        return  context

class Blogcreat(CreateView):
    model = BlogPost
    template_name = 'blog_create.html'
    fields = ['title', 'description', 'image']

class PostListView(ListView):
    template_name = "blog.html"
    queryset: List[BlogPost] = BlogPost.objects.all()
    context_object_name = "blogs"


def create_comment(request, **kwargs):
    post_id = kwargs['pk']
    if request.method == "POST":
        data: dict = request.POST
        if data.get("text"):
            Comment.objects.create(text=data["text"], post_id=post_id)
            return redirect(f'/blog/{post_id}/')
        else:
            return HttpResponse("error")

class PostChangeView(UpdateView):
    model = BlogPost
    fields = {
        "image",
        "title",
        "description"
    }
    template_name = "blog_change.html"