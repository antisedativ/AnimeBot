from router import bot
from aiogram import Dispatcher, types
import requests
import json


async def show_top_handler(mes: types.Message):
    r = requests.get('https://api.jikan.moe/v4/top/anime')

    text = json.loads(r.text)

    names = text['data']
    all_names = ''

    for name in names:
        all_names += f'{name["rank"]}. {name["title"]} {name["score"]}\n'

    chat_id = mes.from_user.id

    await bot.send_message(chat_id, text=all_names)


def register_handlers_show_anime_top(dp: Dispatcher):
    dp.register_message_handler(show_top_handler, commands=['top_anime'])
