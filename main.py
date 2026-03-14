import telebot
import random
import os
from telebot import types
from flask import Flask
from threading import Thread

# --- VEB SERVER QISMI (Render uchun shart) ---
server = Flask('')

@server.route('/')
def home():
    return "Bot is running!"

def run():
    # Render beradigan PORTni oladi, bo'lmasa 8080 ishlatadi
    port = int(os.environ.get("PORT", 8080))
    server.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
# --------------------------------------------

TOKEN = '8786107780:AAGdJ4Z_h0TlKB8SHR-bc0T2pRoyJcEnc6g'
bot = telebot.TeleBot(TOKEN)

# Sizning savollaringiz (LEVELS lug'ati o'zgarishsiz qoladi)
LEVELS = {
    "A1": {
        "name": "🟢 A1 — Beginner",
        "emoji": "🟢",
        "questions_count": 10,
        "questions": [
            {"question": "I ___ a student.", "options": ["am", "is", "are", "be"], "answer": "am"},
            {"question": "She ___ a cat.", "options": ["have", "has", "had", "having"], "answer": "has"},
            {"question": "This is ___ apple.", "options": ["a", "an", "the", "—"], "answer": "an"},
            {"question": "Where ___ you from?", "options": ["is", "am", "are", "be"], "answer": "are"},
            {"question": "What is the plural of 'child'?", "options": ["childs", "children", "childrens", "childes"], "answer": "children"},
            {"question": "He ___ TV every evening.", "options": ["watch", "watches", "watching", "watched"], "answer": "watches"},
            {"question": "We live ___ London.", "options": ["at", "on", "in", "by"], "answer": "in"},
            {"question": "Which word is a NOUN?", "options": ["run", "happy", "teacher", "quickly"], "answer": "teacher"},
            {"question": "___ is your name?", "options": ["Who", "Where", "What", "When"], "answer": "What"},
            {"question": "I have ___ brothers.", "options": ["two", "twos", "second", "twice"], "answer": "two"},
        ]
    },
    # A2, B1, B2, C1 larni o'z joyiga qo'yasiz...
}

LEVEL_ORDER = ["A1", "A2", "B1", "B2", "C1"]
user_data = {}

@bot.message_handler(commands=['start', 'menu'])
def start(message):
    user_data[message.chat.id] = {"state": "choosing_level"}
    show_level_menu(message.chat.id)

def show_level_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for key in LEVEL_ORDER:
        if key in LEVELS: # Xatolikni oldini olish uchun
            markup.add(types.KeyboardButton(LEVELS[key]["name"]))
    bot.send_message(
        chat_id,
        "📚 *English Grammar Quiz*\n\nDarajangizni tanlang:",
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda m: user_data.get(m.chat.id, {}).get("state") == "choosing_level")
def choose_level(message):
    chat_id = message.chat.id
    chosen = next((k for k, v in LEVELS.items() if v["name"] == message.text), None)
    
    if not chosen:
        bot.send_message(chat_id, "❗️ Iltimos, tugmalardan birini tanlang.")
        return

    level = LEVELS[chosen]
    sample_size = min(level["questions_count"], len(level["questions"]))
    selected_questions = random.sample(level["questions"], sample_size)
    
    user_data[chat_id] = {
        "state": "in_quiz",
        "level_key": chosen,
        "score": 0,
        "current_q": 0,
        "questions": selected_questions
    }
    
    bot.send_message(chat_id, f"{level['emoji']} {level['name']} boshlandi!", reply_markup=types.ReplyKeyboardRemove())
    send_question(chat_id)

def send_question(chat_id):
    data = user_data[chat_id]
    q_index = data["current_q"]
    
    if q_index < len(data["questions"]):
        q = data["questions"][q_index]
        options = list(q["options"])
        random.shuffle(options)
        
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        for opt in options:
            markup.add(types.KeyboardButton(opt))
            
        bot.send_message(
            chat_id, 
            f"❓ Savol {q_index+1}/{len(data['questions'])}:\n\n{q['question']}",
            reply_markup=markup
        )
    else:
        finish_quiz(chat_id)

@bot.message_handler(func=lambda m: user_data.get(m.chat.id, {}).get("state") == "in_quiz")
def check_answer(message):
    chat_id = message.chat.id
    if chat_id not in user_data or user_data[chat_id]["state"] != "in_quiz":
        return

    data = user_data[chat_id]
    q_index = data["current_q"]
    correct = data["questions"][q_index]["answer"]

    if message.text == correct:
        data["score"] += 1
        bot.send_message(chat_id, "✅ To'g'ri!")
    else:
        bot.send_message(chat_id, f"❌ Noto'g'ri! To'g'ri javob: *{correct}*", parse_mode="Markdown")

    data["current_q"] += 1
    send_question(chat_id)

def finish_quiz(chat_id):
    data = user_data[chat_id]
    score, total = data["score"], len(data["questions"])
    percent = (score / total) * 100
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🔄 Qaytadan urinish", "📋 Daraja tanlash")
    
    bot.send_message(
        chat_id,
        f"🏁 Quiz tugadi!\n✅ Natija: {score}/{total} ({percent:.0f}%)\n\nNima qilmoqchisiz?",
        reply_markup=markup
    )
    user_data[chat_id] = {"state": "after_quiz", "last_level": data["level_key"]}

@bot.message_handler(func=lambda m: user_data.get(m.chat.id, {}).get("state") == "after_quiz")
def after_quiz_handler(message):
    if message.text == "🔄 Qaytadan urinish":
        level_key = user_data[message.chat.id].get("last_level")
        if level_key:
            message.text = LEVELS[level_key]["name"]
            user_data[message.chat.id]["state"] = "choosing_level"
            choose_level(message)
    else:
        start(message)

if __name__ == "__main__":
    # 1. Avval serverni ishga tushiramiz (Render ko'rishi uchun)
    keep_alive()
    print("🚀 Server va Bot ishga tushdi...")
    # 2. Keyin botni polling qilamiz
    bot.infinity_polling()