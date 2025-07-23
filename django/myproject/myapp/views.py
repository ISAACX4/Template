from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages# Import messages for user feedback
from .models import Feature
# Create your views here.
def index(request):
    features = Feature.objects.all()  # Fetch all Feature objects from the database
    return render(request,'index.html',{'features': features} )#to {'name': name} display names from the backend

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:  # Check if passwords match
           if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                messages.info(request, 'Please use a different email')
                return redirect('register')#returns the user to the registration page after the eamil put already exists
    # Here you would typically save the user to the database
           elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                messages.info(request, 'Please use a different username')
                return redirect('register')
           else:
               user=User.objects.create_user(username=username, email=email, password=password)
               user.save();
               return redirect('login') # Save the user to the database
        
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')# Redirect to the registration page if passwords do not match
    else:
        return render(request, 'register.html');

def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user= auth.authenticate(username=username, password=password)
        if user is not None:#
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials invalid')
            return redirect(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
                                                        
    


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render (request,'counter.html',{'amount':amount_of_words})
#render is used to still stay on thew same page while redirect is to change the page 
def static(request):
     return render (request,'static.html')