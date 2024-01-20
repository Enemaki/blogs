from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import checkowner

from .models import Blog, Tweet
from .forms import BlogForm, TweetForm

# Create your views here.
def index(request):
    """The home page for blogs"""
    tweets = Tweet.objects.get(id=1)
    blogs = tweets.blog
    short_tweet = tweets.text[:100]
    context = {'blogs': blogs, 'tweets': tweets, 'short_tweet': short_tweet}
    return render(request, 'blogs/index.html', context)

def blogs(request):
    """Page for blog topics"""
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """Page for individual posts"""
    blog = Blog.objects.get(id=blog_id)
    tweets = blog.tweet_set.order_by('-date_added')
    context = {'blog': blog, 'tweets': tweets}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    """Add a new blog"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_tweet(request, blog_id):
    """Add a new tweet for a particular blog"""
    blog = Blog.objects.get(id=blog_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TweetForm()
    else:
        # POST data submitted; process data.
        form = TweetForm(data=request.POST)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.blog = blog
            new_tweet.save()
            return redirect('blogs:blog', blog_id=blog_id)
        
    # Display a blank or invalid form.
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_tweet.html', context)

@login_required
def edit_tweet(request, tweet_id):
    """Edit an existing tweet"""
    tweet = Tweet.objects.get(id=tweet_id)
    blog = tweet.blog
    checkowner.check_blog_owner(blog, request)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = TweetForm(instance=tweet)
    else:
        # POST data submitted; process data.
        form = TweetForm(instance=tweet, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)
        
    # Display a blank or invalid form.
    context = {'tweet': tweet, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_tweet.html', context)