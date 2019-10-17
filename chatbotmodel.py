import telegram
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters  # import modules


def get_token():
    file_name = "chatbot_token.json"
    with open(file_name,'r',encoding="UTF8") as data_file:
        data = json.load(data_file)
        print(data)
        token = data["token"]
        print(token)
    return token

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 489724409
        self.name = name
    
    """
    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)
    """
    
    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class ingamsung_bot(TelegramBot):
    def __init__(self):
        self.token = get_token()
        TelegramBot.__init__(self, 'ingamsung', self.token)
        self.updater.stop()
    
    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))
    
    def start(self):
        self.sendMessage(self.id, '해시태그를 입력해주세요.')
        self.updater.start_polling()
        self.updater.idle()
