from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Foydalanuvchilar uchun tugmalar
user_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
user_buttons.add(KeyboardButton("Navbat ro'yxati"))
user_buttons.add(KeyboardButton("Navbatga yozilish"))
user_buttons.add(KeyboardButton("Navbatni bekor qilish"))

# Admin uchun tugmalar
admin_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
admin_buttons.add(KeyboardButton("Navbatni boshlash"))
admin_buttons.add(KeyboardButton("Navbat olish"))
admin_buttons.add(KeyboardButton("Navbat ro'yxati"))
admin_buttons.add(KeyboardButton("Navbatni bekor qilish"))
admin_buttons.add(KeyboardButton("Navbatni yangilash"))
admin_buttons.add(KeyboardButton("Navbatni tasodifiy tanlash"))
