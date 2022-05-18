from carro_api.serializers import CarroSerializer, CarroUpdateSerializer
from libreria_core.models import Carrito
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# agregar el decorador sobre los def
@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def carrito (request):
    if request.method=='GET':
        carrito = Carrito.objects.all()
        serializer = CarroSerializer(carrito, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data =  JSONParser().parse(request)
        serializer = CarroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@api_view(['GET', 'PUT', 'DELETE'])
def libro_carro(request, pk):
    try:
        libro_carro = Carrito.objects.get(codigoCarrito=pk)
    except Carrito.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CarroSerializer(libro_carro)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarroUpdateSerializer(libro_carro, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':

        libro_carro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)