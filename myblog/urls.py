from django.urls import path,include
from. import views
from. views import (
    PostListVeiw,
    PostDtailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListVeiw


)



app_name = 'myblog'
urlpatterns = [
    
    path('', PostListVeiw.as_view(), name='myblog_home'),
    path('user/<str:username>', UserPostListVeiw.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDtailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/',PostCreateView.as_view(), name='post_create'),

    path('like/', views.like_post, name='like-post'),

     #myblog about urls
    path('about/', views.about, name='myblog_about')
    #path('', views.myblog_home, name='myblog_home'),
 ]