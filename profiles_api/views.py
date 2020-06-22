from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format=None):
        """ returns list API features"""
        an_apiview = [
            "Uses HTTP methods as function (get ,psot,patch,put,delete)",
            "is similar to traditional django view",
            "gives you the most control over application logic",
            "is mapped manually to URLS",
        ]

        return Response ({"message":"Hello" ,"an_apiview": an_apiview})
