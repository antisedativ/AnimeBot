from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from private.config import token

bot = Bot(token=token)
dp = Dispatcher(bot)
