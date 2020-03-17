from bs4 import BeautifulSoup
from glob import glob
from random import choice
import requests
import json

from emoji import emojize

from telegram.ext import ConversationHandler
from telegram import ParseMode
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

from utility import get_keyboard
from utility import SMILE




def sms(bot, update):
    # smile = emojize(choice(SMILE), use_aliases=True)
    print('Кто-то отправил команду НАЧАТЬ. Что мне делать?') #вывод сообщения в консоль при отправке команды /start
    bot.message.reply_text('Здравствуйте, {}! \nНажмите'
                           .format(bot.message.chat.first_name), reply_markup=get_keyboard()) # отправим ответ
    print(bot.message)