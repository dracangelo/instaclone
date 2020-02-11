from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreateForm, PostPictureForm, UserUpdateForm, ProfileUpdateForm, CommentForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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





def image_form(request):
    if request.method == 'POST': 
        form = PostPictureForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            # form.save() 
            messages.success(request, f'post created for !')
            return redirect('profile') 
    else: 
        form = PostPictureForm() 
    return render(request, 'image_form.html', {'form' : form}) 





def comment(request, image_id):
    current_user = request.user
    post = Image.objects.get(id=image_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment_form = form.save(commit=False)
            comment_form.user = current_user
            comment_form.image = post
            comment_form.save()

    else:
        form = CommentForm()
    return render(request, 'detail.html', {"form": form, "post": post})

# @login_required(login_url='/accounts/login/')
def update_profile(request):
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request, 'update_profile.html', context)


# @login_required(login_url='/accounts/login/')                
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request, 'profile.html', context)