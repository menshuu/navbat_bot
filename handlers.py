from aiogram import types
from bot import dp, bot
from config import ADMIN_ID
from keyboard import user_buttons, admin_buttons
from queue_system import get_queue_text, add_to_queue, remove_from_queue, reset_queue, shuffle_queue

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """Start komandasi"""
    if message.from_user.id == ADMIN_ID:
        await message.answer("Admin panelga xush kelibsiz!", reply_markup=admin_buttons)
    else:
        await message.answer("Botga xush kelibsiz!", reply_markup=user_buttons)

@dp.message_handler(lambda message: message.text == "Navbat ro'yxati")
async def show_queue(message: types.Message):
    """Navbat ro'yxatini ko'rsatish"""
    await message.answer(get_queue_text())

@dp.message_handler(lambda message: message.text == "Navbatga yozilish")
async def join_queue(message: types.Message):
    """Foydalanuvchini birinchi bo'sh joyga qo'shish"""
    username = f"@{message.from_user.username}" if message.from_user.username else f"ID: {message.from_user.id}"
    for i in range(33):
        if add_to_queue(username, i):
            await message.answer(f"Siz {i+1}-o‘ringa yozildingiz!")
            return
    await message.answer("Afsus, barcha joylar band!")

@dp.message_handler(lambda message: message.text == "Navbatni bekor qilish")
async def leave_queue(message: types.Message):
    """Foydalanuvchini navbatdan chiqarish"""
    username = f"@{message.from_user.username}" if message.from_user.username else f"ID: {message.from_user.id}"
    if remove_from_queue(username):
        await message.answer("Siz navbatdan olib tashlandingiz!")
    else:
        await message.answer("Siz navbatda yo‘qsiz!")

# ADMIN FUNKSIYALARI
@dp.message_handler(lambda message: message.text == "Navbatni boshlash")
async def start_queue(message: types.Message):
    """Admin navbatni boshlaydi"""
    if message.from_user.id == ADMIN_ID:
        await message.answer("Navbat boshlandi!", reply_markup=admin_buttons)
    else:
        await message.answer("Siz admin emassiz!")

@dp.message_handler(lambda message: message.text == "Navbatni yangilash")
async def admin_reset_queue(message: types.Message):
    """Admin butun navbatni tozalaydi"""
    if message.from_user.id == ADMIN_ID:
        reset_queue()
        await message.answer("Navbat yangilandi!", reply_markup=admin_buttons)
    else:
        await message.answer("Siz admin emassiz!")

@dp.message_handler(lambda message: message.text == "Navbatni tasodifiy tanlash")
async def admin_shuffle_queue(message: types.Message):
    """Admin navbatni aralashtiradi"""
    if message.from_user.id == ADMIN_ID:
        shuffle_queue()
        await message.answer("Navbat tasodifiy aralashtirildi!", reply_markup=admin_buttons)
    else:
        await message.answer("Siz admin emassiz!")
