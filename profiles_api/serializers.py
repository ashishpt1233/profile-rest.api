from rest_framework import serializers


class Helloserializer(serializers.Serializer):
    """ Serializer a name field for testing a APIView """
    name = serializers.CharField(max_length=50)
