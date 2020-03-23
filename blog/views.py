from django.shortcuts import render, redirect
from .models import Post
from .models import Reply
from .forms import PostForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.



def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  
        if form.is_valid(): 
            print('hit if')
            form.save()  
            return redirect('blog-home')
        else:
            print('hit else')
            return redirect('blog-home')
            
    # post = Post.objects.create()
    # return render(request, "blog/home.html", context)

def reply_create(request, post_id):
    post = Post.objects.get(id = post_id)
    print(post)
    print('post id: ', post_id)

    # reply = Reply(request.POST.get('input-comment'))
    # reply.post_id = post_id
    # reply.author = request.user
    # reply.save()

    next = request.POST.get('next', '/')
    return redirect(next)
