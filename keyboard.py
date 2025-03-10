from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Foydalanuvchilar uchun tugmalar
user_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
user_keyboard.add(KeyboardButton("Navbat olish"))
user_keyboard.add(KeyboardButton("Navbat ro'yxati"))
user_keyboard.add(KeyboardButton("Navbatni bekor qilish"))

# Admin uchun tugmalar
admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_keyboard.add(KeyboardButton("Navbatni boshlash"))
admin_keyboard.add(KeyboardButton("Navbat olish"))
admin_keyboard.add(KeyboardButton("Navbat ro'yxati"))
admin_keyboard.add(KeyboardButton("Navbatni bekor qilish"))
admin_keyboard.add(KeyboardButton("Navbatni yangilash"))
admin_keyboard.add(KeyboardButton("Navbatni tasodifiy tanlash"))
