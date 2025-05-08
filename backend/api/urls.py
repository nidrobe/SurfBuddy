from django.urls import path
from . import views

urlpatterns = [
    # path('surfboards/', views.SurfboardCreateListView.as_view(), name='surfboard-list'),  # List and create
    # path('surfboards/<int:pk>/', views.SurfboardDeleteView.as_view(), name='delete-surfboard'),  # Retrieve and delete
    path('chat/', views.chat_view, name='chat'), # URL for handling chatbot requests via POST
]