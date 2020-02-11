from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apivew = [
            'Uses HTTP methos as function (get,post,patch,put,delete)',
            'Is similar to a traditiinal Django View',
            'gives you the most control over your application logic',
            'is mapped manuall to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apivew})
