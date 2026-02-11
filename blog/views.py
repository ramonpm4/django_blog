from django.shortcuts import render
from django.http import Http404, HttpResponse
from datetime import date
from .models import Author, Post, Tag

# Create your views here.



my_posts = [
        {
            'slug': 'hike-in-the-mountains',
            'image': 'mountains.jpg',
            'author': 'Ramon',
            'date': date(2026, 2, 8),
            'title': 'Viaje a La Josefina - Saavedra',
            'excerpt': 'En este viaje pude conocer en mayor profundiad la estancia La Josefina. Compartir con mi hermano y aprender de ganaderia regenerativa.',
            'content': """
                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Cum ab voluptates delectus reiciendis esse eos accusamus doloremque 
                sapiente dolorum placeat ipsam repellendus quia, rem quae aut doloribus deserunt maxime incidunt.
            
                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Cum ab voluptates delectus reiciendis esse eos accusamus doloremque 
                sapiente dolorum placeat ipsam repellendus quia, rem quae aut doloribus deserunt maxime incidunt.
            
                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Cum ab voluptates delectus reiciendis esse eos accusamus doloremque 
                sapiente dolorum placeat ipsam repellendus quia, rem quae aut doloribus deserunt maxime incidunt.
            
                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Cum ab voluptates delectus reiciendis esse eos accusamus doloremque 
                sapiente dolorum placeat ipsam repellendus quia, rem quae aut doloribus deserunt maxime incidunt.
            
                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Cum ab voluptates delectus reiciendis esse eos accusamus doloremque 
                sapiente dolorum placeat ipsam repellendus quia, rem quae aut doloribus deserunt maxime incidunt.
                
            """
        },
        {
            "slug": "programming-is-fun",
            "image": "coding.jpg",
            "author": "Maximilian",
            "date": date(2022, 3, 10),
            "title": "Programming Is Great!",
            "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
            "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            """
        },
        {
            "slug": "into-the-woods",
            "image": "woods.jpg",
            "author": "Maximilian",
            "date": date(2020, 8, 5),
            "title": "Nature At Its Best",
            "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
            "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            """
        }]
    
# Helper function:
# def get_date(models.post):
#     return post['date']


def starting_page(request) -> HttpResponse:
    sorted_posts = Post.objects.all().order_by('-date_created') 
    latest_posts = sorted_posts[:3]
    return render(request, "blog/index.html", {
        'latest_posts': latest_posts
    })


def posts(request) -> HttpResponse:
    all_posts = Post.objects.all()
    return render(request, "blog/all-posts.html", {
        'all_posts': all_posts
    })
    
    
def post_detail(request, slug) -> HttpResponse: 
    post = next((p for p in my_posts if p['slug'] == slug), None)
    return render(request, "blog/post_detail.html", {
        'post': post
    })


