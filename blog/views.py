from django.shortcuts import render
from django.http import Http404, HttpResponse
from datetime import date
from .models import Post

# Create your views here.



def starting_page(request) -> HttpResponse:
    latest_posts = Post.objects.all().order_by('-date_created')[:3] #Poner [:3] aca es mejor porque detras hace SQL query para solo los 3. Mas eficiente. 
    return render(request, "blog/index.html", {
        'latest_posts': latest_posts
    })


def posts(request) -> HttpResponse:
    all_posts = Post.objects.all()
    return render(request, "blog/all-posts.html", {
        'all_posts': all_posts
    })
    
    
def post_detail(request, slug) -> HttpResponse: 
    post = Post.objects.get(slug=slug)
    #post = next((p for p in my_posts if p['slug'] == slug), None)
    return render(request, "blog/post_detail.html", {
        'post': post
    })


