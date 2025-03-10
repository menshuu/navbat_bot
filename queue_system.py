import random

# 33 ta joyni bo'sh qilib boshlaymiz
navbatlar = ["Bo'sh"] * 33

def get_queue_text():
    text = "📋 *Navbat ro‘yxati:*\n"
    for number, user in navbatlar.items():
        if user:
            text += f"{number}. @{user['username']}" if user['username'] else f"{number}. {user['name']}\n"
        else:
            text += f"{number}. Bo‘sh\n"
    return text


def add_to_queue(username, index):
    """Foydalanuvchini berilgan joyga qo'shadi."""
    if navbatlar[index] == "Bo'sh":
        navbatlar[index] = username
        return True
    return False

def remove_from_queue(username):
    """Foydalanuvchini navbatdan olib tashlaydi."""
    for i in range(len(navbatlar)):
        if navbatlar[i] == username:
            navbatlar[i] = "Bo'sh"
            return True
    return False

def reset_queue():
    """Navbatni to'liq tozalaydi."""
    global navbatlar
    navbatlar = ["Bo'sh"] * 33

def shuffle_queue():
    """Navbatni tasodifiy aralashtiradi."""
    occupied = [x for x in navbatlar if x != "Bo'sh"]
    random.shuffle(occupied)
    for i in range(len(navbatlar)):
        navbatlar[i] = occupied.pop(0) if occupied else "Bo'sh"
