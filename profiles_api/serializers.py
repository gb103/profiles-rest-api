from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serialize a name field to test ur api view"""
    name = serializers.CharField(max_length=10)
