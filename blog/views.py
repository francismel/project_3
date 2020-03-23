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
    # if request.method == 'POST':
    #     form = RegisterForm(request.POST) #if no files
    #     if form.is_valid():
    #         form.save()
    # context = {
    #     'form': form
    # }
    # return render(request, "blog/home.html", context)
    pass

def comment_create(request, post_id):
    
    next = request.POST.get('next', '/')
    return redirect(next)
