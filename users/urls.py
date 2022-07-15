from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    # static links 
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('search/',views.search,name='search'),
    # path('demo/',views.demo,name='demo'),             # demo url for creating demo profiles


    # dynamic links 
    path('<str:pk>/edit/',views.edit_profile,name='edit_profile'),
    path('<str:pk>/delete/',views.delete_account,name='delete_account'),
    path('<str:pk>/follow/',views.follow,name='follow'),
    path('<str:pk>/unfollow/',views.unfollow,name='unfollow'),
    path('<str:pk>/',views.profile,name='profile'),
]