from django.db import models

# Create your models here.
#You also need to register the models in the ain nproject settings file .go to settings in myproject and under installed apps put in myapp
#migrate the data to the database using cmd  
#type in python manage.py makemigrations in another cmd window go to the directory first 
#and type in python manage.py migrate
#to view the changes in the db just put /admin infront of the server number 
#to know the credentioals in ht e cmd type in manage.py create superuser
#register your models  into the admin.py
class Feature(models.Model):
    name= models.CharField(max_length=100)
    details=models.CharField(max_length=500)
    