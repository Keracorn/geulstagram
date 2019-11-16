import os, io
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler  # import modules
import chatbotmodel
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegram
import json
import re
from chatbotmodel import get_token
import chatbotmodel
from translateAPI import translate_word_eng, translate_word_kor
from search import search
from gptModel import gpt

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'

bot_token = get_token()

ingamsung = telegram.Bot(token=bot_token)
updates = ingamsung.getUpdates()
count = 1


# message reply function
# update is json format

def get_message(bot, update):
    if update.message.text == "bye":
        chat_id = update.message.chat.id
        ingamsung.sendMessage(chat_id, 'Bye!')
        ingamsung.stop()
    else:
        # receiving message and complying automatically
        user_input_text = update.message.text
        msg_id = update.message.message_id
        chat_id = update.message.chat.id
        print(chat_id)

        tag_list = re.findall(r"#(\w+)", user_input_text)
        print(tag_list)

        f = open('tag.txt', 'w')
        f.write(str(tag_list[0]))
        f.close()

        if len(tag_list) == 0:
            update.message.reply_text("아무런 태그를 주지 않으셨어요 ㅠㅠ")
            update.message.reply_text("혹시 해시태그를 붙이셔서 저한테 알려주실래요?")
        else:
            keyboard = [[InlineKeyboardButton("1. 번역", callback_data='1'),
                         InlineKeyboardButton("2. 러닝", callback_data='2')]]

            reply_markup = InlineKeyboardMarkup(keyboard)

            bot.send_message(chat_id, 'Please choose:', reply_markup=reply_markup)


def callback_set(bot, update):
    query = update.callback_query
    data_selected = update.callback_query.data

    # 1번. translate
    if (data_selected == "1"):
        print("1")
        input_sentence = search()
        print(input_sentence)
        translated = translate_word_eng(input_sentence)
        result = translate_word_kor(translated)
        print(result)
        query.edit_message_text(text=result)

    #2번 gpt-model
    if (data_selected == "2"):
        print("2")
        input_sentence = search()
        # query.edit_message_text(text=input_sentence)
        print(input_sentence)
        translated = translate_word_eng(input_sentence)
        print(translated)
        learned_sentence = gpt(translated)
        result = translate_word_kor(learned_sentence[0])
        print(result)
        query.edit_message_text(text=learned_sentence[0])


# bot.editMessageText(chat_id=chat_id, text="Selected option: {}".format(query.data))


updater = Updater(bot_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(callback_set))

ingamsung = chatbotmodel.ingamsung_bot()

updater.start_polling(timeout=3, clean=True)
updater.idle()

ingamsung.start()
