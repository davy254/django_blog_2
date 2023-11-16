from django.urls import path
from .views import hompage


app_name = 'blog'
urlpatterns = [
    path('', hompage , name="homepage")
]
