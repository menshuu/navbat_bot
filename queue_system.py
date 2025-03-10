import random
from config import MAX_NAVBAT

navbatlar = {i: None for i in range(1, MAX_NAVBAT + 1)}

def get_queue_text():
    text = "📋 *Navbat ro‘yxati:*\n"
    for number, user in navbatlar.items():
        if user:
            text += f"{number}. @{user['username']}" if user['username'] else f"{number}. {user['name']}\n"
        else:
            text += f"{number}. Bo‘sh\n"
    return text

def reset_queue():
    global navbatlar
    navbatlar = {i: None for i in range(1, MAX_NAVBAT + 1)}

def shuffle_queue():
    global navbatlar
    occupied_slots = [k for k, v in navbatlar.items() if v]
    random.shuffle(occupied_slots)
    new_navbatlar = {i: None for i in range(1, MAX_NAVBAT + 1)}
    for i, slot in enumerate(occupied_slots, start=1):
        new_navbatlar[i] = navbatlar[slot]
    navbatlar = new_navbatlar
