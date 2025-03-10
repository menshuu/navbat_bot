from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def user_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("📋 Navbat ro‘yxati", callback_data="show_list"))
    keyboard.add(InlineKeyboardButton("📝 Navbatga yozilish", callback_data="register"))
    keyboard.add(InlineKeyboardButton("❌ Navbatni bekor qilish", callback_data="cancel_queue"))
    return keyboard

def admin_menu():
    keyboard = user_menu()
    keyboard.add(InlineKeyboardButton("🔄 Navbatni yangilash", callback_data="reset_queue"))
    keyboard.add(InlineKeyboardButton("🎲 Navbatni tasodifiy tanlash", callback_data="shuffle_queue"))
    keyboard.add(InlineKeyboardButton("🚀 Navbatni boshlash", callback_data="start_queue"))
    return keyboard

def navbat_olish_tugmalari(available_slots):
    keyboard = InlineKeyboardMarkup(row_width=4)
    for number in available_slots:
        keyboard.insert(InlineKeyboardButton(str(number), callback_data=f"take_{number}"))
    return keyboard
