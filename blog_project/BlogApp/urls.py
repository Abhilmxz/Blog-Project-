from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_blog_posts, name='list_blog_posts'),
    path('post/<int:pk>/', views.view_blog_post, name='view_blog_post'),
    path('post/new/', views.create_blog_post, name='create_blog_post'),
    path('post/<int:pk>/edit/', views.edit_blog_post, name='edit_blog_post'),
    path('post/<int:pk>/delete/', views.delete_blog_post, name='delete_blog_post'),
]
