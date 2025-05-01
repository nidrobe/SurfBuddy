from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, SurfboardSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from .models import Surfboard
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # TODO: Restrict this in production

# TODO: Add error handling 
class SurfboardCreateListView(generics.ListCreateAPIView):
    queryset = Surfboard.objects.all()
    serializer_class = SurfboardSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['name', 'brand', 'type'] # Allows searching by name, brand, or type

# TODO: Add error handling
class SurfboardDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Surfboard.objects.all()
    serializer_class = SurfboardSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([AllowAny])  # Allow any user (authenticated or not)
def test_endpoint(request):
    return Response({"message": "Backend is connected!"})
