from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer #,SurfboardSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
# from .models import Surfboard
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from django.conf import settings
import logging

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # TODO: Restrict this in production

# # TODO: Add error handling 
# class SurfboardCreateListView(generics.ListCreateAPIView):
#     queryset = Surfboard.objects.all()
#     serializer_class = SurfboardSerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends = [SearchFilter]
#     search_fields = ['name', 'brand', 'type'] # Allows searching by name, brand, or type

# # TODO: Add error handling
# class SurfboardDeleteView(generics.RetrieveDestroyAPIView):
#     queryset = Surfboard.objects.all()
#     serializer_class = SurfboardSerializer
#     permission_classes = [IsAuthenticated]

# Get an instance of a logger
logger = logging.getLogger(__name__)
# logger.info("Testing logging from urls.py")

# Initialize OpenAI Client
client = OpenAI(api_key=settings.OPENAI_API_KEY)
# logger.info(f"Key loaded: {settings.OPENAI_API_KEY}")


# Define the Chat View
@api_view(['POST'])  
@permission_classes([AllowAny])  # Allow any user 
def chat_view(request):
    if request.method == 'POST':
        try:
            # logger.info("Received a POST request")
            user_message = request.data.get('message', '')
            # logger.info(f"Received message: {user_message}")

            logger.info(f"Full request data: {request.data}")  # Check the whole request
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=100
            )
            # logger.info(f"Full OpenAI API response: {response}")
            ai_message = response.choices[0].message.content
            logger.info(f"AI Response: {ai_message}")  # log ai message before returning
            return Response({'message': ai_message}, status=status.HTTP_200_OK)  # Use DRF's Response

        
        except Exception as e:
            logger.exception(f"Error processing request: {e}")  # Log the full exception
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  

    return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST) 

