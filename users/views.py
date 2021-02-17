from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm


# Create your views here.

def register(request):
    #makin a user registration 
    if request.method == 'POST':
        #proceed data
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You account has been created! You are now able to login')
            return redirect('login')
    else:
        #great an empty form   
        #form = UserCreationForm()
         form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,
                                       instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, f'You account has been updatad!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    
    context={
         'user_form': user_form,
         'profile_form': profile_form

    }

    return render(request, 'users/profile.html', context)