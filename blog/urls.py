from django.urls import path
from .views import PostDeleteView, hompage, post_detail, PostCreateView, PostUpdateView, Post


app_name = 'blog'
urlpatterns = [
    path('', hompage , name="homepage"),
    path('<int:pk>/', post_detail, name='post-detail' ),
    path('create-post/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),


]
