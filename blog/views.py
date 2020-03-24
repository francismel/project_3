from django.shortcuts import render, redirect
from .models import Post
from .models import Reply
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.



def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)


def post_create(request):
    post = Post( author = request.user, strContent = request.POST.get('post-input') )
    print(post)
    post.save()
    next = request.POST.get('currentpath', '/')
    return redirect(next)

def reply_create(request, post_id):
    post = Post.objects.get(id = post_id)
    reply = Reply( author = request.user, post = post, strContent = request.POST.get('input-comment') )
    reply.save()
    next = request.POST.get('currentpath', '/')
    return redirect(next)
