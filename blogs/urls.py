from django.urls import path, include
from .views import (
    BlogDeleteView,
    BlogDetailView,
    BlogListView,
    BlogUpdateView,
    BlogCreateView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="list_blogs"),
    path("post/createblog/", BlogCreateView.as_view(), name="create_blog"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="detailed_blog"),
    path("post/<int:pk>/udpate", BlogUpdateView.as_view(), name="update_blog"),
    path("post/<int:pk>/delete", BlogDeleteView.as_view(), name="delete_blog"),
]
