from django.urls import path
from .views import hompage, post_detail


app_name = 'blog'
urlpatterns = [
    path('', hompage , name="homepage"),
    path('<int:post_id>/', post_detail, name='post-detail' ),
]
