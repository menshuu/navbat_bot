from aiogram import executor
from bot import dp
import handlers  # Barcha handlerlar yuklanishi uchun import qilinadi

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
