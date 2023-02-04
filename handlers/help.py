from aiogram import types, Dispatcher
import json
from router import bot

with open('handlers/comands.json', encoding="utf-8") as f:
    comands = json.load(f)['items']

async def help_handler(mes: types.Message):
    all_commands = 'описание бота \n\n'
    for com in comands:
        all_commands += f'{com["name"]} - {com["discription"]}\n'
        #print(com)
    chat_id = mes.from_user.id
    await bot.send_message(chat_id, text=all_commands)


def register_handlers_help(dp: Dispatcher):
    dp.register_message_handler(help_handler, commands=['help'])
