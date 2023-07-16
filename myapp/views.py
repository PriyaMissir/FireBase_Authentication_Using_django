# from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages

import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyBKmMkOE0QuLgLBw2-Prq3gWvGcUz17N0A",
  'authDomain': "fir-authentication-aabe3.firebaseapp.com",
  'databaseURL': "https://fir-authentication-aabe3-default-rtdb.firebaseio.com",
  'projectId': "fir-authentication-aabe3",
  'storageBucket': "fir-authentication-aabe3.appspot.com",
  'messagingSenderId': "625103438647",
  'appId': "1:625103438647:web:0bce87f8f096e405d910b2",
}



firebase=pyrebase.initialize_app(firebaseConfig)
auth= firebase.auth()
database=firebase.database()
# from django.contrib.auth.models import User

def signUp(request):
    return render(request,'registration.html')

def signIn(request):
    return render(request,'login.html')

def profile(request):
    user = auth.current_user
    if user:
        
       
            
            uid = user['uid']
            display_name = user['displayName']
            email = user['email']
           
            context = {
            'name': display_name,
            'email': email,
         
             }
            return render(request, "index.html", context)
    else:
            return redirect("signIn")
    

   


def register(request):
     email = request.POST.get('email')
     password = request.POST.get('password')
     name = request.POST.get('name')
     
     try:
        # creating a user with the given email and password
        user=auth.create_user_with_email_and_password(email,password)
        messages.success(request,"Registeration is successfull")
        

     except:
         messages.error(request,"This email already exits!!!!")
         return redirect('signUp')
     return render(request, "login.html")
 
def userLogin(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    try:
        user=auth.sign_in_with_email_and_password(email,password)
        messages.success(request,"Logged In")
        if request.user.is_authenticated:
            print(request.user.is_authenticated)
            return render(request,'index.html')
        else:
       
           return redirect('login')  
    except:
        messages.error(request,"Error")
        return redirect('signIn')
    
   
     
def userLogout(request):
    try:
        del request.session['uid']
        messages.success(request,"Logged Out...")
    except:
        pass
       
    messages.error(request,"Error in logged out")
    return redirect("signIn")


def reset(request):
    return render(request, "reset.html")
 
def postReset(request):
    email = request.POST.get('email')
    try:
        auth.send_password_reset_email(email)
        messages.success(request,"Email to reset password is successfully sent")
        return render(request, "Reset.html")
    except:
        messages.error(request,"Something went wrong, Please check the email you provided is registered or not")
        return render(request, "Reset.html")
    
    