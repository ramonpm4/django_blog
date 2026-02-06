from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.



my_posts = [
    {'title': 'The real man', 'slug':'the-real-man', 'content': 'This is my first post.'},
    {'title': 'Why you should learn django.','slug': 'why-to-learn-django' , 'content': 'Why you should learn django.'}
]


def starting_page(request) -> HttpResponse:
    return render(request, "blog/index.html", {
        'blog_section': 'Posts'
    })



def posts(request) -> HttpResponse:
    return render(request, "blog/all-posts.html")
    
    
def post_detail(request, slug) -> HttpResponse: 
    return render(request, "blog/post_detail.html")


