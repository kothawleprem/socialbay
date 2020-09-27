from django.contrib import admin
from django.urls import path, include
from .views import PostCreateView
from django.conf import settings



from . import views

urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', views.blogPost, name='blogPost'),
   # path('blog/<str:username>',UserPostListView.as_view(), name='user-post'),
    #path('<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    #path('<int:pk>/delete', PostDeleteView.as_view(), name='post-delete')
    #path('<str:slug>', views.blogPost, name='blogPost'),
    
]


handler404 = 'blog.views.error_404_view'