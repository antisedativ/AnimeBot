from router import bot
from aiogram import Dispatcher, types
import requests


async def show_top_handler(mes: types.Message):
    r = requests.get('https://api.jikan.moe/v4/top/anime')



    chat_id = mes.from_user.id
    s = 'TOP anime'
    await bot.send_message(chat_id, text=s)


def register_handlers_show_top(dp: Dispatcher):
    dp.register_message_handler(show_top_handler, commands=['top_anime'])
