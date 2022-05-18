from rest_api.serializers import LibroSerializer, UpdateStockSerializer
from libreria_core.models import Libro
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# agregar el decorador sobre los def
@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def libros (request):
    if request.method=='GET':
        lista_libro = Libro.objects.all()
        serializer = LibroSerializer(lista_libro, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data =  JSONParser().parse(request)
        serializer = LibroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@api_view(['GET', 'PUT', 'DELETE'])
def libro(request, pk):
    try:
        libro = Libro.objects.get(codigo=pk)
    except Libro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LibroSerializer(libro)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UpdateStockSerializer(libro, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':

        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)