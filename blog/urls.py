from django.urls import path
from .views import PostDeleteView, hompage, post_detail, PostCreateView, PostUpdateView, Post


app_name = 'blog'
urlpatterns = [
    path('', hompage , name="homepage"),
    path('create-post/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/', post_detail, name='post-detail' ),
    path('post/<slug:slug>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete', PostDeleteView.as_view(), name='post-delete'),


]
