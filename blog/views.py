from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.



my_posts = {
    'The real man': 'Content: The real man',
    'Why you should learn django.': 'Content: Why you should learn django.'
}


def home_blog(request) -> HttpResponse:
    return render(request, "blog/home.html", {
        'blog_section': 'Home'
    })



def index(request) -> HttpResponse:
    posts = list(my_posts.keys())
    return render(request, "blog/index.html", {
        'posts' : posts
    })
    
    
def post_content(request, post) -> HttpResponse:
    try:
        post_text = my_posts[post]
        return render(request, "blog/post_content.html", {
            'text': post_text,
            'selected_post': post
        })
    except:
        raise Http404