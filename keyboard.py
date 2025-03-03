from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_ID

def user_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("📋 Navbat ro‘yxati"))
    keyboard.add(KeyboardButton("📝 Navbat olish"), KeyboardButton("❌ Navbatimni bekor qilish"))
    return keyboard

def admin_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("🚀 Navbatni boshlash"))
    keyboard.add(KeyboardButton("📝 Navbat olish"), KeyboardButton("📋 Navbat ro‘yxati"))
    keyboard.add(KeyboardButton("❌ Navbatni bekor qilish"), KeyboardButton("🔄 Navbatni yangilash"))
    keyboard.add(KeyboardButton("🎲 Navbatni tasodifiy tanlash"))
    return keyboard

def navbat_raqamlari(navbatlar):
    keyboard = InlineKeyboardMarkup()
    for number, user in navbatlar.items():
        if user is None:
            keyboard.add(InlineKeyboardButton(str(number), callback_data=f"take_{number}"))
    return keyboard
