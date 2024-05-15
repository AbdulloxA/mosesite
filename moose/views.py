from django.shortcuts import render
from .models import BlogPost,About,ContactMe,Home,Bloglar

# Create your views here.

def index(request):
    home = Home.objects.all()
    blogss = Bloglar.objects.all()
    cxt = {
        "home": home,
        "blogss":blogss
    }
    return render(request, 'index.html',cxt)


def blog(request):
    blogs = BlogPost.objects.all()
    cxt = {
        "blogs": blogs
    }
    return render(request, 'blog.html',cxt)


def about(request):
    abouts = About.objects.all()
    cxt = {
        "abouts":abouts
    }
    return render(request, 'about.html',cxt)


def contact(request):
    contacts = ContactMe.objects.all()
    cxt = {
        "contacts": contacts
    }
    return render(request, 'contact.html',cxt)
