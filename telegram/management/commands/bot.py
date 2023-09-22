from django.core.management.base import BaseCommand
from django.conf import settings
import telebot

from telegram.models import TelegramUser


# Объявление переменной бота
bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


# Название класса обязательно - "Command"
class Command(BaseCommand):
    help = 'Launches a Telegram bot and saves messages as tokens.'

    def handle(self, *args, **kwargs):
        # Инициализируем бота
        bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)

        # Обработчик команды /start
        @bot.message_handler(commands=['start'])
        def handle_start(message):
            bot.send_message(message.chat.id, "Здравствуйте! Любое ваше сообщение будет записано как новый токен!")

        # Обработчик всех сообщений
        @bot.message_handler(func=lambda message: True)
        def handle_message(message):
            chat_id = message.chat.id
            token = message.text

            # Создаем или обновляем запись в таблице TelegramUser
            telegram_user, created = TelegramUser.objects.get_or_create(chat_id=chat_id)
            telegram_user.token = token
            telegram_user.save()

            bot.send_message(chat_id, f'Сохранено как новый токен: {chat_id} - {token}')

        # Запускаем бота
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()