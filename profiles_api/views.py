from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


class HelloApiView(APIView):
    """Test Api view"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""

        as_apiview = [ 'in general support functions (get, post, delete, update)',
        'is similar tp traditional django views',
        'provide better control over application logic',
        'is mapped manually to urls'
        ]

        return Response({'message':'Hello!', 'as_apiview':as_apiview})

    def post(self, request):
        """Returns a Hello message of requester name"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """update complete object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """partially update  object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """delete complete object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test Api view set"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""

        a_viewset = [
        'Uses actions (list, create, retrieve, update, partial_update)',
        'automiatically maps to urls using routers',
        'provide more functionaltiy with less code'

        ]

        return Response({'message':'hello a view set', 'a_viewset' : a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})
