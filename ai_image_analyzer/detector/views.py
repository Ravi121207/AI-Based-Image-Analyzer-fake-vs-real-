from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,ImageForm
from .models import ImageUpload
from .fake_real_detector import analyze_image
import os


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request,'detector/register.html',{'form':form})


def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('dashboard')

    return render(request,'detector/login.html')


@login_required
def dashboard(request):

    form = ImageForm()

    if request.method == "POST":

        form = ImageForm(request.POST,request.FILES)

        if form.is_valid():

            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            result = analyze_image(obj.image.path)

            obj.result = result
            obj.save()

            return render(request,'detector/result.html',{'obj':obj})

    return render(request,'detector/dashboard.html',{'form':form})


def user_logout(request):

    logout(request)
    return redirect('login')
