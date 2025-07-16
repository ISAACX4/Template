from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
def index(request):
    feature1= Feature()
    feature1.id=0
    feature1.name="fast"
    feature1.details="Our services is very quick"
    
    feature2= Feature()
    feature2.id=1
    feature2.name="Reliable"
    feature2.details="Our services is reliable "
    
    feature3= Feature()
    feature3.id=2
    feature3.name="Easy to use"
    feature3.details="Our services is very easy to use"
    
    feature4= Feature()
    feature4.id=3
    feature4.name="affordable"
    feature4.details="Our services is very affordable"
    
    
    features=[feature1, feature2, feature3,feature4]
    
    return render(request,'index.html',{'features': features} )#to {'name': name} display names from the backend

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render (request,'counter.html',{'amount':amount_of_words})

def static(request):
     return render (request,'static.html')