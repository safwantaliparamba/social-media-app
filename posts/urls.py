from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('<str:user_id>/create/',views.create_post,name='create_post'),
    path('<str:pk>/view/',views.single_post,name='single_post'),
    path('<str:pk>/edit/',views.edit_post,name='edit_post'),
    path('<str:pk>/delete/',views.delete_post,name='delete_post'),
    path('<str:post_id>/like/',views.like_post,name='like_post'),
]