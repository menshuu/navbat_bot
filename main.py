import asyncio
from aiogram import Bot, Dispatcher
from bot import dp, bot  # `bot.py` ichida `bot` va `dp` bo‘lishi kerak

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

