from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .models import Post, Category
from .forms import PostForm, UpdateForm

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-post_date"]

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:

        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:

        category_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = stuff.total_likes()

        context["category_menu"] = category_menu
        context["total_likes"] = total_likes
        
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "update_post.html"

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")

class AddCategoryView(CreateView):
    model = Category
    fields = "__all__"
    template_name = "add_category.html"

def CategoryView(request, category):

    category_posts = Post.objects.filter(category=category.replace("-", " "))

    return render(request, "category.html", {"category": category.replace("-", " "), "category_posts": category_posts})

def CategoryListView(request):

    category_menu_list = Category.objects.all()

    return render(request, "category_list.html", {"category_menu_list": category_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))