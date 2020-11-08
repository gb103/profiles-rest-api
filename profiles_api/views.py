from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api view"""
    def get(self, request, format=None):
        """Return a list of APIView features"""

        as_apiview = [ 'in general support functions (get, post, delete, update)',
        'is similar tp traditional django views',
        'provide better control over application logic',
        'is mapped manually to urls'
        ]

        return Response({'message':'Hello!', 'as_apiview':as_apiview})
