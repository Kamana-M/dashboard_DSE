from django.urls import path #Allows us to add multiple url on our list
from . import views #. represent the root file

"""We will put all the url we have on our project in urlpatterns
    To specify new url we use path we are declaring a new url. When we just put '' it represent the main/first/home path of our app
    name represent the ID """
urlpatterns=[
    path('', views.LOG, name='log'), 
    path('CARDS', views.CARDS, name='cards') 
    ] 




