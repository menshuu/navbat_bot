from aiogram import types
from bot import dp, bot
from config import ADMIN_ID
from keyboard import user_keyboard, admin_keyboard

# Navbatni saqlash uchun ro‘yxat
queue = []


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
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.full_name

    if user_id not in [user["id"] for user in queue]:  # Agar foydalanuvchi navbatda bo‘lmasa
        queue.append({"id": user_id, "name": username})
        await message.answer(f"✅ {username}, siz navbatga qo‘shildingiz!\n\n" + get_queue_list())
    else:
        await message.answer("⛔ Siz allaqachon navbatdasiz!")


# Navbat ro‘yxati
@dp.message_handler(lambda message: message.text == "Navbat ro'yxati")
async def show_queue(message: types.Message):
    await message.answer(get_queue_list())


# Navbatni bekor qilish
@dp.message_handler(lambda message: message.text == "Navbatni bekor qilish")
async def cancel_queue(message: types.Message):
    global queue
    user_id = message.from_user.id

    queue = [user for user in queue if user["id"] != user_id]
    await message.answer("❌ Sizning navbatingiz bekor qilindi!")


# Navbatni yangilash (Admin)
@dp.message_handler(lambda message: message.text == "Navbatni yangilash")
async def refresh_queue(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        global queue
        queue.clear()
        await message.answer("🔄 Navbat yangilandi!")
    else:
        await message.answer("⚠️ Siz bu amalni bajara olmaysiz!")


# Navbat ro‘yxatini chiqaruvchi funksiya
def get_queue_list():
    if not queue:
        return "📭 Navbat hozircha bo‘sh!"

    text = "📋 **Navbat ro‘yxati:**\n"
    for idx, user in enumerate(queue, start=1):
        text += f"{idx}. {user['name']}\n"

    return text
