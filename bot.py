import time
import logging

from aiogram import Bot, Dispatcher, executor, types

from message_text import GREETINGS

logging.basicConfig(level=logging.INFO)

token = '5348905024:AAFvyCI45ECONooqFP5U1JWFjwHnunfJB5U'

photo = 'https://avatanplus.com/files/resources/original/58f1ea455683515b70fb1eea.png'
admin_chat_id = 1050726426

bot = Bot(token=token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(mes: types.Message):
    print(mes)
    chat_id = mes.from_user.id
    user_first_name = mes.chat.first_name

    await bot.send_photo(chat_id, photo=photo, caption=GREETINGS.format(user_first_name))


if __name__ == '__main__':
    executor.start_polling(dp)
