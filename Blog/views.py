from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q 
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import CommentForm

class BlogView(ListView):
    template_name = "blog.html"
    model = Blogs
    context_object_name = "posts"

    def get_queryset(self):
        category = self.request.GET.get("category")
        author = self.request.GET.get("author")
        if category:
            self.queryset = Blogs.objects.filter(category__name = category).order_by("-date").all()[:4]
        elif author:
            self.queryset = Blogs.objects.filter(author__author_slug = author).order_by("-date").all()[:4]
        else:
            self.queryset = Blogs.objects.order_by("-date").all()[:4]
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['p_posts'] = Blogs.objects.order_by("-read_count").all()[:4]
        context['categories'] = Categories.objects.all()
        return context

class BlogDetailView(DetailView, CreateView):
    template_name = 'blog_detail.html'
    slug_url_kwarg = 'slug'
    model = Blogs
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        blog = Blogs.objects.get(slug=self.kwargs.get("slug"))
        blog.read_count += 1
        blog.save()
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return Blogs.objects.get(slug=self.kwargs.get("slug"))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.blog = Blogs.objects.get(slug=self.kwargs.get("slug"))
            comments.save()
        return redirect('blog_detail', slug=self.kwargs.get("slug"))

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['r_blogs'] = Blogs.objects.filter(~Q(slug = self.kwargs.get("slug"))).all()[:5]
        context['p_posts'] = Blogs.objects.order_by("-read_count").all()[:4]
        context['categories'] = Categories.objects.all()
        context['comments'] = Comments.objects.filter(blog__slug = self.kwargs.get("slug")).order_by("-date").all()[:5]
        return context
