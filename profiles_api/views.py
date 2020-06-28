from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

class HelloApiView(APIView):
    serializer_class = serializers.Helloserializer
    def get(self, request, format=None):
        """ returns list API features"""
        an_apiview = [
            "Uses HTTP methods as function (get ,psot,patch,put,delete)",
            "is similar to traditional django view",
            "gives you the most control over application logic",
            "is mapped manually to URLS",
        ]

        return Response ({"message":"Hello" ,"an_apiview": an_apiview})

    def post(self,request):
        """Create a hello  message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        """Handling update a object"""
        return Response({'method': 'PUT'})

    def patch(self, request ,pk=None):
        """Handle a partial update of an object """
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.Helloserializer

    def list(self,request):

        a_viewset = [
        'uses actions (list,create,retreive,update,partial_update)',
        'Automatically more functionality with less code',
        'Provides more functionality with less code',
        ]

        return Response ({'message':'Hello', 'a_viewset':a_viewset})

    def create(self,request):
        """Create anew hello message """
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'hello {name}!!'
            return Response ({"message": message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ handle getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'Delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Hanlde creating and updating profile"""
    serializer_class=serializers.UserProfileSerialiser
    queryset=models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes= (permissions.UpdateOwnProfile,)
