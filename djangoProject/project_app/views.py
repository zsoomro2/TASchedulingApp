from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('login')
        else:
            messages.success(request, "There was an error logging in, please try again")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    pass