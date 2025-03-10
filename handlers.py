from aiogram import types
from bot import dp, bot
from config import ADMIN_ID
from queue_system import navbatlar, get_queue_text, reset_queue, shuffle_queue
from keyboard import user_menu, admin_menu, navbat_olish_tugmalari

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("👋 Admin paneliga xush kelibsiz!", reply_markup=admin_menu())
    else:
        await message.answer("👋 Xush kelibsiz! \nBu bot orqali navbat olish mumkin.", reply_markup=user_menu())

@dp.callback_query_handler(lambda c: c.data == "show_list")
async def show_list(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, get_queue_text(), parse_mode="Markdown")

@dp.callback_query_handler(lambda c: c.data == "register")
async def register(callback_query: types.CallbackQuery):
    available_slots = [num for num, user in navbatlar.items() if user is None]
    if available_slots:
        await bot.send_message(callback_query.from_user.id, "⏳ Qaysi navbatni tanlaysiz?", reply_markup=navbat_olish_tugmalari(available_slots))
    else:
        await bot.send_message(callback_query.from_user.id, "❌ Hamma joy band!")

@dp.callback_query_handler(lambda c: c.data.startswith("take_"))
async def take_slot(callback_query: types.CallbackQuery):
    number = int(callback_query.data.split("_")[1])
    if navbatlar[number] is None:
        user = callback_query.from_user
        navbatlar[number] = {"name": user.full_name, "username": user.username}
        await bot.send_message(callback_query.from_user.id, f"✅ Siz {number}-navbatni oldingiz!\n\n{get_queue_text()}", parse_mode="Markdown")
    else:
        await bot.send_message(callback_query.from_user.id, "❌ Bu joy allaqachon band!")

@dp.callback_query_handler(lambda c: c.data == "reset_queue")
async def reset_queue_handler(callback_query: types.CallbackQuery):
    if callback_query.from_user.id == ADMIN_ID:
        reset_queue()
        await bot.send_message(callback_query.from_user.id, "♻️ Navbat yangilandi!")
    else:
        await bot.send_message(callback_query.from_user.id, "❌ Sizda bu amalni bajarish huquqi yo‘q!")

@dp.callback_query_handler(lambda c: c.data == "shuffle_queue")
async def shuffle_queue_handler(callback_query: types.CallbackQuery):
    if callback_query.from_user.id == ADMIN_ID:
        shuffle_queue()
        await bot.send_message(callback_query.from_user.id, "🎲 Navbat tasodifiy joylashtirildi!")
    else:
        await bot.send_message(callback_query.from_user.id, "❌ Sizda bu amalni bajarish huquqi yo‘q!")
