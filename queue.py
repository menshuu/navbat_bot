from config import MAX_NAVBAT
import random

navbatlar = {i: None for i in range(1, MAX_NAVBAT + 1)}

def reset_queue():
    global navbatlar
    navbatlar = {i: None for i in range(1, MAX_NAVBAT + 1)}

def shuffle_queue():
    global navbatlar
    users = [user for user in navbatlar.values() if user is not None]
    random.shuffle(users)
    for i, user in enumerate(users):
        navbatlar[i + 1] = user

def get_queue_text():
    text = "📋 *Navbat ro‘yxati:*\n"
    for number, user in navbatlar.items():
        text += f"{number}. {user if user else 'Bo‘sh'}\n"
    return text
