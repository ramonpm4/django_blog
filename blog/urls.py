from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_blog),
    path("posts", views.index, name='post-index'), # type: ignore
    path("<str:post>", views.post_content, name='post-content'),
]
