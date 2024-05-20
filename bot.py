import telebot
from googletrans import Translator
from langdetect import detect


API_TOKEN = '<api_token>'
bot = telebot.TeleBot(API_TOKEN)

translator = Translator()

#Исходный язык и целевой язык
src = 'jp'
dest = 'ru'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
こんにちは！
Здравствуйте! 
Я бот-переводчик японского языка. Приятно познакомиться！(´• ω •`). Я могу вам перевести предложение на японский язык, но к сожалению я не могу вам обещать перевод любого предложения так как существуют некоторые нюансы...
В общем, если хотите, чтобы я вам перевел что-нибудь, то можете написать просто предложение и я сразу же переведу  :)
Если возникли какие то трудности, то можете обратиться ко мне с командой "/help". 
私は日本語のボットです。初めまして！(´• ω •`)。私は文を翻訳することができます。\
""")

#Функция для обработки сообщений
@bot.message_handler(func=lambda m: True)
def translate_message(message):
    src = detect(message.text)                                                           #----------------------------------------------Исходный язык исходного текста
    dest = 'ru'                                                                          #----------------------------------------------Целевой язык
    translated_text = translator.translate(message.text, src=src, dest=dest).text        #----------------------------------------------Полученное сообщение, перевод
    bot.send_message(message.chat.id, translated_text)                                   # ---------------------------------------------Переведенное сообщение


bot.infinity_polling()