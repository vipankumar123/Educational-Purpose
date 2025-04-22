from rest_framework import serializers

class ColorSerializer(serializers.Serializer):
    name = serializers.CharField()
