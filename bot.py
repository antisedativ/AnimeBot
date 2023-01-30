# import time
import logging

from aiogram import Bot, Dispatcher, executor, types

from message_text import GREETINGS
from services.db import db_connect, db_add_user, db_show_users, db_close, db_show_count_users

logging.basicConfig(level=logging.INFO)

token = '5348905024:AAFvyCI45ECONooqFP5U1JWFjwHnunfJB5U'

# Пнг приветствия
photo = 'https://avatanplus.com/files/resources/original/58f1ea455683515b70fb1eea.png'

# Мой chat_id
admin_chat_id = 1050726426

bot = Bot(token=token)
dp = Dispatcher(bot=bot)


async def on_startup(_):
    await db_connect()


@dp.message_handler(commands=['start'])
async def start_handler(mes: types.Message):
    await db_add_user(mes.from_user.id,
                      mes.from_user.username,
                      mes.from_user.first_name,
                      mes.from_user.last_name,
                      mes.date)

    print(mes)

    chat_id = mes.from_user.id
    user_first_name = mes.chat.first_name

    print('#'*20)
    print(f'У бота новое сообщение от: {user_first_name}, в {mes.date}')
    print('#' * 20)

    await bot.send_photo(chat_id, photo=photo, caption=GREETINGS.format(user_first_name))


# Выводит всех пользователей из бд (нужно сделать приватной)
@dp.message_handler(commands=['show_users'])
async def show_users_handler(mes: types.Message):
    count = await db_show_count_users()
    await bot.send_message(admin_chat_id, f'В настоящий момент у бота - {count} пользователей')
    await db_show_users()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
