from django.urls import path
from .views import (
                    PostListView,
                    PostDetailView,             
                    PostDeleteView,
                    UserPostListView
                    )
from . import views

app_name = "blog"
urlpatterns = [
    path('post/update/<int:pk>/',views.postUpdate,name='post-update'),
    path('user/<str:username>/',UserPostListView.as_view(),name='user-posts'),
    #path('user/<str:username>/',views.profilePost,name='user-posts'),
    path('post/delete/<int:pk>/',PostDeleteView.as_view(), name='post-delete'),
    path('',PostListView.as_view() ,name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view() ,name='blog-home-post'),
    path('post_form/',views.postCreate ,name='post-create'),
    path('about/', views.about,name='blog-about'),
    path('post/likes/<int:pk>/',views.like,name='like'),
    path('comment/<int:pk>',views.addComment,name = "comment"),
    path('comment/<int:pk>/remove/',views.commentRemove,name = "comment_remove")
]


