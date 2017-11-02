from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# url would call these functions

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
        .order_by('-published_date')
    # here 'posts' is passed to the for loop in the .html file
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

