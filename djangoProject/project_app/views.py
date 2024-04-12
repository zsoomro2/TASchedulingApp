from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from .models import MyUser

# Create your views here.
class Login(View) :
    def get(self, request):
        return render(request, "login.html", {})
    def post(self, request):
        noSuchUser = False
        badPassword = False
        try:
            m = MyUser.objects.get(name=request.POST['username'])
            badPassword = (m.password != request.POST['password'])
        except:
            noSuchUser = True
        if noSuchUser:
            m = MyUser(name=request.POST['name'], password=request.POST['password'])
            m.save()
            request.session['username'] = m.username
            return redirect('/home/')
        elif badPassword:
            return render(request, "login.html", {"msg": "Bad password"})
        else:
            request.session['username'] = m.username
            return redirect('/home/')


def logout_user(request):
    pass