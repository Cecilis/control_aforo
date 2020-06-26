from rest_framework import serializers


class MonitorSerializer(serializers.Serializer):
    mwf = serializers.CharField(max_length=20)
    mbt = serializers.CharField(max_length=20)

class MonitorLinkSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=255)
    token = serializers.CharField(max_length=700)

class MonitorFSSerializer(serializers.Serializer):
    camara = serializers.CharField(max_length=20)
    zona = serializers.CharField(max_length=100)
