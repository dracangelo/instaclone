from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreateForm, ProfileForm, PostPictureForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, Profile





# Create your views here.

def landing(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'index.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('signup_success.html')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})  



def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})


def logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")


def signup_success(request):

     
    return render(request, 'signup_success.html')


def success(request): 
    return HttpResponse('successfully uploaded')


def image_view(request): 
  
    if request.method == 'POST': 
        form = PostPictureForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = PostPictureForm() 
    return render(request, 'image_form.html', {'form' : form}) 


def profile(request):
    current_user = request.user
    posts = Post.get_posts()
    comments = Comment.get_comments()
    return render(request, 'profile.html', {'current_user':current_user, 'posts':posts, 'comments':comments})


def update_profile(request):
    current_user = request.user
    # profile = Profile(User=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user= current_user
            profile.save()
        return redirect('home')
    # else:
    #     # form = ProfileForm(instance=request.user.profile)
    #     args = {}
    #     args['form'] = form
    return render(request, 'update_profile.html', {'current_user':current_user,})
