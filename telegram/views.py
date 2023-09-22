from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .models import TelegramUser, Message
import telebot
from .serializers import MessageSerializer, RegistrationSerializer

# Инициализация бота
bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        message = serializer.save(user=user)

        try:
            telegram_user = TelegramUser.objects.get(token=request.auth)
            chat_id = telegram_user.chat_id

            bot.send_message(chat_id, f'{(user.first_name).title()}, я получил от тебя сообщение:\n{message.message_text}')
        except TelegramUser.DoesNotExist:
            return Response({'error': 'Пользователь с таким токеном не найден в базе данных'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)


@permission_classes([IsAuthenticated])
class MessageList(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Message.objects.filter(user=user)
        return queryset
