from django.urls import path
from .views import (
    PostListView, PostDetailView, PostUpdateView, PostDeleteView, PostCreateView, UserPostListView, CommentCreateView, LikeView)
from django.urls import path
from users import views as auth_views
from . import views

urlpatterns = [
    path('about/', views.about, name='blog-about'),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-dateil'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/comment', CommentCreateView.as_view(), name='add_comment'),
]