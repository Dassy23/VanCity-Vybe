from django.urls import path
from . import views

urlpatterns = [

path('', views.allposts, name='posts'),
path('post/<post_id>/', views.postdetail, name='post_detail'),

]
