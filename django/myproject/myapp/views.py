from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html',)#to {'name': name} display names from the backend

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render (request,'counter.html',{'amount':amount_of_words})

def static(request):
     return render (request,'static.html')