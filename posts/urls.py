from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('<str:user_id>/create/',views.create_post,name='create_post'),
    path('<str:pk>/view/',views.single_post,name='single_post'),
]