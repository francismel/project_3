from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post', views.post_create, name='post_create'),
    path('reply/post/<int:post_id>', views.reply_create, name='reply_create'),
]
