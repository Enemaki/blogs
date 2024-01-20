from django.http import Http404
def check_blog_owner(blog, request):
    """Checks if blog owner is the same as user"""
    if blog.owner != request.user:
        raise Http404