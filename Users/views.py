from allauth.account.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login,authenticate

# Create your views here.
from .models import BlogUser


def register_view(request):
    if request.method=='GET':
        return render(request,'registration.html')

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password2 != password:
            return HttpResponse("Passwords does not match!!!")
        user = BlogUser.objects.create_user(username='awdawd', first_name=first_name,last_name=last_name,age=age,email=email,
                                            password=password)

        return HttpResponse("Registered successfully!!!")



def login_view(request):
    if request.method=='GET':
        return render(request,'login.html')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user= authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return  redirect('blogs')

        return render(request,'login.html',context={"message":"Не правильный логин или пароль!!!"})

from django.contrib import auth
def logout_view(request):

    auth.logout(request)
    return redirect('/Users/login/')

class MyLoginView(LoginView):
    template_name = 'login.html'

