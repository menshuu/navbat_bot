from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Command  # BU YERNI TO‘G‘RILANDI
from aiogram.utils import executor

TOKEN = "7923166429:AAG6JQH1xfilj8135oe-fKjC-IGNnw48RNE"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Salom! Botga xush kelibsiz!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
