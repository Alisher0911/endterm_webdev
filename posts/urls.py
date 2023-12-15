# from django.urls import path
# from posts import views

# urlpatterns = [
#     path("", views.home),
#     path("posts/<int:post_id>/", views.posts),
# ]
from django.urls import path
from posts.views import PostListCreateView, PostDetailView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]