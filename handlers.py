from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from bot import dp, bot
from keyboard import user_buttons, admin_buttons, get_queue_buttons

# Foydalanuvchilar uchun navbat ma'lumotlari
queue = {}

# Admin ID (bu yerda o'z Telegram ID raqamingizni yozing)
ADMIN_ID = 123456789

# Botni ishga tushirganda foydalanuvchilarga xush kelibsiz xabari
@dp.message_handler(Command("start"))
async def send_welcome(message: types.Message):
    welcome_text = (
        "Assalomu alaykum! Ushbu bot orqali siz navbatga yozilishingiz mumkin.\n"
        "Quyidagi tugmalar yordamida kerakli amallarni bajaring."
    )
    if message.from_user.id == ADMIN_ID:
        await message.answer(welcome_text, reply_markup=admin_buttons)
    else:
        await message.answer(welcome_text, reply_markup=user_buttons)

# Navbat olish tugmasi
@dp.message_handler(lambda message: message.text == "Navbat olish")
async def get_queue(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("Quyidagi joylardan birini tanlang:", reply_markup=get_queue_buttons(queue))
    else:
        await message.answer("Quyidagi joylardan birini tanlang:", reply_markup=get_queue_buttons(queue))

# Foydalanuvchi joy tanlaganda
@dp.callback_query_handler(lambda call: call.data.startswith("slot_"))
async def select_slot(call: types.CallbackQuery):
    slot_number = int(call.data.split("_")[1])
    user_id = call.from_user.id
    user_name = call.from_user.username or call.from_user.full_name

    if slot_number not in queue:
        queue[slot_number] = user_name
        await bot.answer_callback_query(call.id, f"Siz {slot_number}-joyni oldingiz!")
    else:
        await bot.answer_callback_query(call.id, "Bu joy allaqachon band!")

    await bot.send_message(call.message.chat.id, "Yangilangan navbat ro'yxati:\n" + get_queue_list())

# Navbat ro'yxatini ko'rsatish
@dp.message_handler(lambda message: message.text == "Navbat ro'yxati")
async def show_queue(message: types.Message):
    await message.answer("Hozirgi navbat ro'yxati:\n" + get_queue_list())

def get_queue_list():
    text = ""
    for i in range(1, 34):
        if i in queue:
            text += f"{i}. {queue[i]}\n"
        else:
            text += f"{i}. Bo'sh\n"
    return text

# Admin "Navbatni boshlash" tugmasini bossa, navbat yangilanadi
@dp.message_handler(lambda message: message.text == "Navbatni boshlash")
async def start_queue(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        queue.clear()
        await message.answer("Navbat yangilandi! Foydalanuvchilar endi navbat olishlari mumkin.", reply_markup=admin_buttons)

# Admin "Navbatni yangilash" tugmasini bossa, butun navbat tozalanadi
@dp.message_handler(lambda message: message.text == "Navbatni yangilash")
async def refresh_queue(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        queue.clear()
        await message.answer("Navbat butunlay yangilandi!", reply_markup=admin_buttons)

# Admin "Navbatni tasodifiy tanlash" tugmasi
@dp.message_handler(lambda message: message.text == "Navbatni tasodifiy tanlash")
async def shuffle_queue(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        import random
        shuffled_queue = list(queue.values())
        random.shuffle(shuffled_queue)
        queue.clear()
        for i, user in enumerate(shuffled_queue, start=1):
            queue[i] = user
        await message.answer("Navbat tasodifiy tartibda aralashtirildi:\n" + get_queue_list())

# Navbatni bekor qilish tugmasi
@dp.message_handler(lambda message: message.text == "Navbatni bekor qilish")
async def cancel_slot(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username or message.from_user.full_name

    for slot, name in queue.items():
        if name == user_name:
            del queue[slot]
            await message.answer(f"{slot}-joyingiz bekor qilindi.")
            return
    await message.answer("Sizda band qilingan joy yo‘q.")
