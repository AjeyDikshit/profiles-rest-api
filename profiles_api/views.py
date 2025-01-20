from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns list of APIViews features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete',
            "Is similar to traditional django view",
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

