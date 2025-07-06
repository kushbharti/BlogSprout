from django.shortcuts import render,redirect
from .models import Blogpost
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    all_blogs = Blogpost.objects.all().order_by('-created_day')
    return render(request,'home.html',{'all_blogs':all_blogs})

def user_posts(request):
    posts =Blogpost.objects.filter(author =request.user).order_by('-created_day')
    
    return render(request,'blog_user_post.html',{'posts':posts})

def create_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog_post = form.save(commit = False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('home')
    else:
        form = BlogForm()
        
    return render(request,'create_blog.html',{'form':form})

def delete_post(request,slug_post):
    post = Blogpost.objects.get(slug_post=slug_post)
    post.delete()
    return redirect('user_posts')

def update_post(request,slug_post):
    post = Blogpost.objects.get(slug_post=slug_post)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('user_posts')
    else:
        form = BlogForm(instance=post)
    return render(request,'update_post.html',{'form':form,'post':post})