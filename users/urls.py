from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('search/',views.search,name='search'),
    path('<str:pk>/',views.profile,name='profile'),
    path('<str:pk>/edit/',views.edit_profile,name='edit_profile'),
    path('<str:pk>/delete/',views.delete_account,name='delete_account'),
    path('<str:pk>/follow/',views.follow,name='follow'),
    path('<str:pk>/unfollow/',views.unfollow,name='unfollow')
]