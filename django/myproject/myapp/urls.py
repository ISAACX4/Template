from django.urls import path
from . import views

#urls.py is like a a mpa that tells django what to don when someone visits a certain web address on your site e.g
#when someone goes to www.mywebsite.com/contact django needs to know "what should i show the user when they go to /contact"
urlpatterns = [
    path('', views.index, name='index'),
    path('counter',views.counter,name='counter'),
    path('static',views.static,name='static'),#static is the name of the html file,then it tells me to go to view folder and loacte the static module
    path('register',views.register,name='register'),
    path('login',views.login, name='login'),# for creating logon page
    path('logout',views.logout,name='logout')
    ]