from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from handlers import dp  # `handlers.py` faylingizda `dp` aniqlangan bo‘lishi kerak

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
