from router import bot
from aiogram import Dispatcher, types


async def start_handler(mes: types.Message):
    # await db_add_user(mes.from_user.id,
    #                   mes.from_user.username,
    #                   mes.from_user.first_name,
    #                   mes.from_user.last_name,
    #                   mes.date)

    print('mes')

    # Пнг приветствия
    PHOTO = 'https://avatanplus.com/files/resources/original/58f1ea455683515b70fb1eea.png'
    GREETINGS = """Приветствую {}!

    Я Senpai-бот, создан облегчить тебе жизнь
    """
    chat_id = mes.from_user.id
    user_first_name = mes.chat.first_name

    print('#' * 20)
    print(f'У бота новое сообщение от: {user_first_name}, в {mes.date}')
    print('#' * 20)

    await bot.send_photo(chat_id, photo=PHOTO, caption=GREETINGS.format(user_first_name))


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
