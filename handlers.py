from aiogram import types
from aiogram.dispatcher.filters import Command
from bot import dp, bot
from config import ADMIN_ID
from keyboard import user_menu, admin_menu, navbat_raqamlari
from queue import navbatlar, reset_queue, shuffle_queue, get_queue_text

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("👋 Admin, boshqaruv menyusi:", reply_markup=admin_menu())
    else:
        await message.answer("👋 Assalomu alaykum! \nBu bot orqali navbat olish mumkin.", reply_markup=user_menu())

@dp.message_handler(lambda message: message.text == "📋 Navbat ro‘yxati")
async def show_list(message: types.Message):
    await message.answer(get_queue_text(), parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "📝 Navbat olish")
async def register(message: types.Message):
    await message.answer("⏳ Qaysi navbatni tanlaysiz?", reply_markup=navbat_raqamlari(navbatlar))

@dp.callback_query_handler(lambda c: c.data.startswith("take_"))
async def take_slot(callback_query: types.CallbackQuery):
    number = int(callback_query.data.split("_")[1])
    if navbatlar[number] is None:
        navbatlar[number] = callback_query.from_user.full_name
        await bot.send_message(callback_query.from_user.id, f"✅ Siz {number}-navbatni oldingiz!\n\n{get_queue_text()}", parse_mode="Markdown")
    else:
        await bot.send_message(callback_query.from_user.id, "❌ Bu navbat allaqachon band qilingan!")

@dp.message_handler(lambda message: message.text == "❌ Navbatimni bekor qilish")
async def cancel_slot(message: types.Message):
    for number, user in navbatlar.items():
        if user == message.from_user.full_name:
            navbatlar[number] = None
            await message.answer("✅ Sizning navbat bekor qilindi.")
            return
    await message.answer("❌ Sizda band qilingan navbat yo‘q.")

@dp.message_handler(lambda message: message.text == "🔄 Navbatni yangilash")
async def admin_reset_queue(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        reset_queue()
        await bot.send_message(message.chat.id, "♻️ *Navbat yangilandi!*", parse_mode="Markdown")
        await bot.send_message(message.chat.id, get_queue_text(), parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "🎲 Navbatni tasodifiy tanlash")
async def admin_shuffle_queue(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        shuffle_queue()
        await bot.send_message(message.chat.id, "🔀 *Navbat random tartibda joylashtirildi!*", parse_mode="Markdown")
        await bot.send_message(message.chat.id, get_queue_text(), parse_mode="Markdown")
