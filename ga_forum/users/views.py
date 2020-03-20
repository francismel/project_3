from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Profile
from django.contrib.auth.decorators import login_required




def registerUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Congrats {username} on your new account!')
            # new_profile = Profile(form)
            # new_profile.save()
            return redirect('blog-home')

    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form': form})

@login_required
def viewProfile(request):
    return render(request,'users/profile.html')