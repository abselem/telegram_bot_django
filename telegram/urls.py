from django.urls import path
from . import views

urlpatterns = [
    path('create_message/', views.create_message, name='create_message'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('messages/', views.MessageList.as_view(), name='message-list'),
]