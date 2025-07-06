from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('create_post/',views.create_post,name='create_post'),
    path('user_posts/',views.user_posts,name='user_posts'),
    path('delete_post/<slug:slug_post>',views.delete_post,name ='delete_post'),
    path('update_post/<slug:slug_post>',views.update_post,name='update_post'),
]