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
    return render(request, "blog/posts.html", {
        'posts' : my_posts
    })
    
    
def post_detail(request, slug) -> HttpResponse:
    
    try:
        selected_post = next(p for p in my_posts if p['slug'] == slug)
        return render(request, "blog/post_detail.html", {
            'text': selected_post["content"],
            'title': selected_post["title"]
        })
    except:
        raise Http404