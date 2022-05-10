from django.urls import path
from rest_api.views import libros_comprados_api, libro_comprado_api
from rest_api.viewsLogin import login

urlpatterns = [
    path('libros', libros_comprados_api, name='libros_comprados'),
    path('libro', libro_comprado_api, name='libro_comp'),
    path('login', login, name='login'),
]