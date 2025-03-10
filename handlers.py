from aiogram import types
from bot import dp, bot
from config import ADMIN_ID
from keyboard import user_keyboard, admin_keyboard

# Start komandasi
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("Salom Admin! Sizning buyruqlaringiz:", reply_markup=admin_keyboard)
    else:
        await message.answer("Salom! Navbat olish yoki ko‘rish uchun tugmalarni bosing.", reply_markup=user_keyboard)

# Navbat olish
@dp.message_handler(lambda message: message.text == "Navbat olish")
async def get_queue(message: types.Message):
    await message.answer("Siz navbat olish tugmasini bosdingiz!")

# Navbat ro‘yxati
@dp.message_handler(lambda message: message.text == "Navbat ro'yxati")
async def show_queue(message: types.Message):
    await message.answer("Hozircha navbatlar yo‘q!")

# Navbatni bekor qilish
@dp.message_handler(lambda message: message.text == "Navbatni bekor qilish")
async def cancel_queue(message: types.Message):
    await message.answer("Sizning navbatingiz bekor qilindi!")

# Faqat adminlar uchun
@dp.message_handler(lambda message: message.text == "Navbatni yangilash")
async def refresh_queue(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("Navbat yangilandi!")
    else:
        await message.answer("Siz bu amalni bajara olmaysiz!")

