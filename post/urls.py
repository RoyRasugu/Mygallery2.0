from post.views import favorite, index, NewPost, PostDetails, tags, like
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('newpost/', NewPost, name='newpost'),
   	path('<uuid:post_id>', PostDetails, name='postdetails'),
   	path('<uuid:post_id>/like', like, name='postlike'),
   	path('<uuid:post_id>/favorite', favorite, name='postfavorite'),
   	path('tag/<slug:tag_slug>', tags, name='tags'),
]