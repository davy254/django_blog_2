from django.urls import path
from .views import hompage, post_detail, PostCreateView


app_name = 'blog'
urlpatterns = [
    path('', hompage , name="homepage"),
    path('<int:pk>/', post_detail, name='post-detail' ),
    path('create-post/', PostCreateView.as_view(), name='post-create'),
]
