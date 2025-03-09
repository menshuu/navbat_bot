from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Foydalanuvchi tugmalari
user_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
user_buttons.add(KeyboardButton("Navbat olish"))
user_buttons.add(KeyboardButton("Navbat ro'yxati"))
user_buttons.add(KeyboardButton("Navbatni bekor qilish"))

# Admin tugmalari
admin_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
admin_buttons.add(KeyboardButton("Navbatni boshlash"))
admin_buttons.add(KeyboardButton("Navbat olish"))
admin_buttons.add(KeyboardButton("Navbat ro'yxati"))
admin_buttons.add(KeyboardButton("Navbatni bekor qilish"))
admin_buttons.add(KeyboardButton("Navbatni yangilash"))
admin_buttons.add(KeyboardButton("Navbatni tasodifiy tanlash"))

# Navbatdagi joylarni tanlash uchun tugmalar
def get_queue_buttons(queue):
    markup = InlineKeyboardMarkup()
    for i in range(1, 34):
        if i not in queue:
            markup.add(InlineKeyboardButton(text=str(i), callback_data=f"slot_{i}"))
    return markup
