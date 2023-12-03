from django.shortcuts import render
from .models import Post

def page1(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})