"""Defines URL patter for blogs"""
from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for the blog topics
    path('blogs/', views.blogs, name='blogs'),
    # Page for individual posts
    path('blog/<int:blog_id>/', views.blog, name='blog'),
    # Page for adding a new blog
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page for adding a new entry
    path('new_tweet/<int:blog_id>/', views.new_tweet, name='new_tweet'),
    # Page for editing a tweet
    path('edit_tweet/<int:tweet_id>/', views.edit_tweet, name='edit_tweet'),
]
