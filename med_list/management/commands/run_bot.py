from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async
from telegram import ParseMode

from django.conf import settings
from django.core.management.base import BaseCommand

from med_list.models import Drug


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Введите название препарата, чтобы узнать работает ли он')


@run_async
def find_drug(update, context):
    try:
        drug = Drug.objects.get(names__contains=[update.message.text])
        analogs = Drug.objects.exclude(id=drug.id).filter(description=drug.description)

        text_parts = [f'Название: {update.message.text}']
        if analogs:
            analog_strings = []
            for drug in analogs:
                analog_strings.append('/'.join(drug.names))

            analogs_string = ', '.join(analog_strings)
            text_parts.append(f'Аналоги: {analogs_string}')
        text_parts.append(f'Описание: {drug.description.description}')

        text = '\n\n'.join(text_parts)
    except Drug.DoesNotExist:
        text = f'По вашему запросу "{update.message.text}" ничего не найдено'

    context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


class Command(BaseCommand):
    help = 'Run telegram bot'

    def handle(self, *args, **kwargs):
        updater = Updater(token=settings.TELEGRAM_TOKEN, use_context=True)
        dispatcher = updater.dispatcher

        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)

        drug_handler = MessageHandler(Filters.text, find_drug)
        dispatcher.add_handler(drug_handler)

        updater.start_polling()
