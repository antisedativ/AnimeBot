from aiogram import types
async def show_top_handler(mes: types.Message):
    comands = []
    all_names = ''

    for name in names:
        all_names += f'{name["rank"]}. {name["title"]} {name["score"]}\n'

    chat_id = mes.from_user.id

    await bot.send_message(chat_id, text=all_names)
