from django.contrib.auth.models import User
from rest_framework import serializers
# from .models import Surfboard

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    Handles serialization and deserialization of User objects.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    # Create a new user within the database
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
# class SurfboardSerializer(serializers.ModelSerializer):
#     """
#     Serializer for the Surfboard model.
#     Handles serialization and deserialization of Surfboard objects.
#     """
#     class Meta:
#         model = Surfboard
#         fields = '__all__'
#         extra_kwargs = {
#             'length_units': {'default': 'feet'},
#             'width_units': {'default': 'inches'},
#             'thickness_units': {'default': 'inches'},
#             'volume_units': {'default': 'liters'},
#         }