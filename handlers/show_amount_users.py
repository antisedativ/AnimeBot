from aiogram import types, Dispatcher
from router import bot

from database.db import db_show_users, db_show_count_users


# Выводит всех пользователей из бд (нужно сделать приватной)
async def show_users_handler(mes: types.Message):
    chat_id = mes.from_user.id
    count = await db_show_count_users()
    await bot.send_message(chat_id, f'В настоящий момент у бота - {count} пользователей')
    await db_show_users()


def register_handlers_show_amount_user(dp: Dispatcher):
    dp.register_message_handler(show_users_handler, commands=['show_users'])
