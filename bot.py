import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

TOKEN = os.getenv("7923166429:AAG6JQH1xfilj8135oe-fKjC-IGNnw48RNE")  # Tokenni Render yoki .env faylga joylashtiring

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
