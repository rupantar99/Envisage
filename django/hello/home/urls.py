from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
   path('',views.index,name="home"),
   path('about',views.about,name="home"),
   path('services',views.services,name="home"),
   path('book',views.contact,name="home"),
   path('contact',views.contact,name="home"),
   path('team',views.team,name="home"),
   path('signup',views.Signup.as_view(),name="signup")
]
