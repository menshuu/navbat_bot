import sqlite3
from config import DB_NAME

# 🔹 Baza yaratish
def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS queue (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        slot INTEGER)''')
    conn.commit()
    conn.close()

# 🔹 Bo'sh joylarni olish
def get_empty_slots():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT slot FROM queue")
    occupied_slots = [row[0] for row in cursor.fetchall()]
    all_slots = list(range(1, 34))
    empty_slots = [slot for slot in all_slots if slot not in occupied_slots]
    conn.close()
    return empty_slots

# 🔹 Navbatga yozish
def add_to_queue(user_id, slot):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO queue (user_id, slot) VALUES (?, ?)", (user_id, slot))
    conn.commit()
    conn.close()

# 🔹 Foydalanuvchini tekshirish
def user_in_queue(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT slot FROM queue WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# 🔹 Navbatni bekor qilish
def remove_from_queue(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM queue WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

# 🔹 Navbatni tozalash
def reset_queue():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM queue")
    conn.commit()
    conn.close()
