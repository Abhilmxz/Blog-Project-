from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})

def list_blog_posts(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'list_blog_posts.html', {'blog_posts': blog_posts})

def view_blog_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'view_blog_post.html', {'blog_post': blog_post})

def edit_blog_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('view_blog_post', pk=pk)
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'edit_blog_post.html', {'form': form, 'blog_post': blog_post})

def delete_blog_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        blog_post.delete()
        return redirect('list_blog_posts')
    return render(request, 'delete_blog_post.html', {'blog_post': blog_post})