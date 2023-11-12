from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView, CategoryListView

urlpatterns = [
    path("", HomeView.as_view(), name = "home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("add_post", AddPostView.as_view(), name = "add_post"),
    path("article/<int:pk>/edit", UpdatePostView.as_view(), name = "update_post"),
    path("article/<int:pk>/delete", DeletePostView.as_view(), name = "delete_post"),
    path("add_category", AddCategoryView.as_view(), name = "add_category"),
    path("categories/<str:category>/", CategoryView, name = "category"),
    path("categories/", CategoryListView, name = "category-list"),
    path("like/<int:pk>/", LikeView, name = "like_post"),
]
