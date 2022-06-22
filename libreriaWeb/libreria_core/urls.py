from django.urls import path
from .views import home
#Urls que tendra libreria#

urlpatterns = [
    path ('', home, name= "inicio"),

] 

