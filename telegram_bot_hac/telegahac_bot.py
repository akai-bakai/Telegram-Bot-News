import telebot
import requests
from Mytoken import token
from telebot import types
import parser

bot = telebot.TeleBot(token)

url = 'https://kaktus.media/?date=2020-11-29&lable=8&order=main#paginator'
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'
           }




# КНОПКА СТАРТА И ЗАПРОС НА ВСЕ НОВОСТИ:
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет! Для вывода новостей напиши мне все новости')



# ПАРСИНГ ВСЕ НОВОСТИ И НУМЕРАЦИЯ:
def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response

@bot.message_handler(func=lambda message: True)
def get_message(message):
    message_text = message.text
    chat_id = message.chat.id
    if message_text == 'все новости':
        find_all_news(chat_id)
    else:
        find_this_news(message_text, chat_id)

def find_all_news(chat_id):
    bot.send_message(chat_id, str(hackaton.news_headers))
    bot.send_message(chat_id, 'А теперь напиши номер заголовка который тебя заинтересовал')


def find_this_news(message_text, chat_id):
    bot.send_message(chat_id, str(hackaton.get_content(hackaton.html.text, int(message_text))))

@bot.message_handler(commands=['quit'])
def quit(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Досвидание', reply_markup=inline_keyboard)

bot.polling()



