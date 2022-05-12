from django.urls import path
from rest_api.views import libros, libro
from rest_api.viewsLogin import login

urlpatterns = [
    path('libros', libros, name='libros'),
    path('libro/<pk>', libro, name='libro'),
    path('login', login, name='login'),
]