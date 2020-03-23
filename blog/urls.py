from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('post', views.post_create, name='post_create'),
    path('comment/post/<int:post_id>', views.comment_create, name='comment_create'),
]
