from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return s list of APIVIEW features"""
        an_apiview = [
            'Hello', 'hai'

        ]

        return Response({'message':'hello', 'an_apiview' : an_apiview})
