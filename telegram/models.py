from django.db import models
from django.contrib.auth.models import User  # Предполагается, что вы используете стандартную модель User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    message_text = models.TextField()  # Текст сообщения
    date_sent = models.DateTimeField(auto_now_add=True)  # Дата и время отправки сообщения

    def __str__(self):
        return f"Message from {self.user.username} at {self.date_sent}"


class TelegramUser(models.Model):
    chat_id = models.CharField(max_length=255, unique=True)
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.chat_id