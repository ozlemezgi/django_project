from django.urls import path
from .views import (
                    PostListView,
                    PostDetailView,             
                    PostDeleteView
                    )
from . import views

app_name = "blog"
urlpatterns = [
    path('post/<int:id>/<int:pk>/update/',views.postUpdate,name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name='post-delete'),
    path('',PostListView.as_view() ,name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view() ,name='blog-home-post'),
    path('post_form/',views.postCreate ,name='post-create'),
    path('about/', views.about,name='blog-about'),
]


