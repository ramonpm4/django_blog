from django.shortcuts import render
from django.http import Http404, HttpResponse
from datetime import date

# Create your views here.



my_posts = [
        {
            'slug': 'hike-in-the-mountains',
            'image': 'mountains.jpg',
            'author': 'Ramon',
            'date': date(2026, 2, 8),
            'title': 'Viaje a La Josefina - Saavedra',
            'excert': 'En este viaje pude conocer en mayor profundiad la estancia La Josefina. Compartir con mi hermano y aprender de ganaderia regenerativa.',
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
    



def starting_page(request) -> HttpResponse:
    return render(request, "blog/index.html", {
        'blog_section': 'Posts'
    })



def posts(request) -> HttpResponse:
    return render(request, "blog/all-posts.html")
    
    
def post_detail(request, slug) -> HttpResponse: 
    return render(request, "blog/post_detail.html")


