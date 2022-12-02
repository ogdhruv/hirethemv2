from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name: str = "blogs/create_blog.html"
    success_url = reverse_lazy("list_blogs")
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogListView(ListView):
    model = Post
    template_name: str = "blogs/blogs.html"
    context_object_name = "all_blogs"
    paginate_by: int = 10


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name: str = "blogs/detailed_blog.html"
    context_object_name: str = "blog"


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name: str = "blogs/update_blog.html"
    context_object_name: str = "blog"
    fields = ["title", "body"]
    success_url = reverse_lazy("list_blogs")


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name: str = "blogs/delete_blog.html"
    success_url = reverse_lazy("list_blogs")
