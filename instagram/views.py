from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import UserCreateForm
# Create your views here.
def landing(request):
   

    return render(request,'index.html')


def signup(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username'])
            profile = UserProfile(user=user)
            profile.save()

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('index')

    return render(request, 'signup.html', {
        'form': form
    })