from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from django.contrib import messages
from .form import *
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"companymeet.html")
def contact(request):
    return render(request,"contact.html")
def signup(request):
    return render(request,"signup.html")
def team(request):
    return render(request,"team.html")
class Signup(View):
    def get(self,request):
        fm=SignupForm()
        return render(request,"signup.html",{'form':fm})
    def post(self,request):
        fm=SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Sign up sucess!!")
            return redirect("/signup")
        else:
            return render(request,"signup.html",{'form':fm})