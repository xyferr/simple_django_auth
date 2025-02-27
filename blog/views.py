from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

# Doctor: Create a new blog post
@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('dashboard')  # Redirect to doctor's dashboard
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})

# Doctor: View their own blog posts
@login_required
def doctor_blog_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'doctor_blog_posts.html', {'posts': posts})

from collections import defaultdict

# Patient: View all published blog posts
def patient_blog_posts(request):
    posts = BlogPost.objects.filter(status='published')
    #print components of posts here for debugging
    for p in posts:
        print(p.id)
        print()
        
    
    return render(request, 'patient_blog_posts.html', {'posts': posts})

# Patient: View a single blog post
def blog_post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id, status='published')
    return render(request, 'blog_post_detail.html', {'post': post})