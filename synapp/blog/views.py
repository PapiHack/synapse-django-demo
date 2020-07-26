from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', { 'posts': posts })

def add_post(request):
    if request.method == 'POST':
        form = request.POST
        post = Post(title=form['title'], content=form['content'])
        post.save()
        return redirect(home)
    return render(request, 'blog/add.html')

def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = request.POST
        post.title = form['title']
        post.content = form['content']
        post.save()
        return redirect(home)
    return render(request, 'blog/edit.html', locals())

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/detail.html', locals())

def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect(home)
