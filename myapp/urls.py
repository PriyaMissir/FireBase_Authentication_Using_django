from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [   
               
  
   path(' ',views.signIn,name='signIn'),
   path('signUp/',views.signUp,name='signUp'),
   path('register/',views.register,name='register'),
   path('userLogin/',views.userLogin,name='login'),
   path('userLogout/',views.userLogout,name='logout'),
   path('reset/', views.reset),
   path('postReset/', views.postReset),
   path('profile/',views.profile,name='profile'),
  
]
