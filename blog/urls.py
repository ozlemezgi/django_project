from django.urls import path
from .views import (
                    PostListView,
                    PostDetailView)
from . import views

app_name = "blog"
urlpatterns = [
    path('',PostListView.as_view() ,name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view() ,name='blog-home-post'),
    path('post_form/',views.postCreate ,name='post-create'),
    path('about/', views.about,name='blog-about'),
]


