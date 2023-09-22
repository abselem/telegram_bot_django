from django.contrib import admin
from .models import *


class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_text', 'date_sent')


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'token')


admin.site.register(Message, MessageAdmin)
admin.site.register(TelegramUser, TelegramUserAdmin)
