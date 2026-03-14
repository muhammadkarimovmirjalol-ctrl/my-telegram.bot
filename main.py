import telebot
import random
from telebot import types

# ⚠️ DIQQAT: @BotFather dan olgan YANGI tokenni shu yerga qo'ying!
TOKEN = '8241530988:AAEWqBJhQZR7G5b5MCnaL4Xbe_MHtJHpUXw'
bot = telebot.TeleBot(TOKEN)

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
    "A2": {
        "name": "🔵 A2 — Elementary",
        "emoji": "🔵",
        "questions_count": 10,
        "questions": [
            {"question": "Yesterday, I ___ a movie.", "options": ["watch", "watches", "watched", "will watch"], "answer": "watched"},
            {"question": "Look! It ___ right now.", "options": ["is raining", "rained", "rains", "will rain"], "answer": "is raining"},
            {"question": "I ___ my wallet last night. I can't find it!", "options": ["lose", "lost", "am losing", "will lose"], "answer": "lost"},
            {"question": "What ___ you do last weekend?", "options": ["do", "does", "did", "will"], "answer": "did"},
            {"question": "She is ___ than her sister.", "options": ["tall", "taller", "tallest", "more tall"], "answer": "taller"},
            {"question": "Have you ___ sushi before?", "options": ["eat", "ate", "eaten", "eating"], "answer": "eaten"},
            {"question": "I ___ to the gym three times a week.", "options": ["go", "went", "gone", "going"], "answer": "go"},
            {"question": "He ___ his bike to work every day.", "options": ["ride", "rides", "rode", "riding"], "answer": "rides"},
            {"question": "We ___ dinner when the phone rang.", "options": ["have", "had", "were having", "will have"], "answer": "were having"},
            {"question": "I promise I ___ you tomorrow.", "options": ["call", "called", "will call", "am calling"], "answer": "will call"},
        ]
    },
    "B1": {
        "name": "🟡 B1 — Intermediate",
        "emoji": "🟡",
        "questions_count": 10,
        "questions": [
            {"question": "She has lived here ___ 5 years.", "options": ["since", "for", "during", "while"], "answer": "for"},
            {"question": "If it rains, we ___ stay at home.", "options": ["will", "would", "should", "shall"], "answer": "will"},
            {"question": "The report ___ by tomorrow morning.", "options": ["will finish", "will be finished", "is finishing", "finishes"], "answer": "will be finished"},
            {"question": "I wish I ___ harder at school.", "options": ["study", "studied", "had studied", "will study"], "answer": "had studied"},
            {"question": "She asked where I ___.", "options": ["live", "lived", "was living", "had lived"], "answer": "lived"},
            {"question": "He ___ for 3 hours when she finally called.", "options": ["waited", "was waiting", "had been waiting", "has waited"], "answer": "had been waiting"},
            {"question": "By next year, she ___ her degree.", "options": ["finish", "finished", "will have finished", "finishes"], "answer": "will have finished"},
            {"question": "The bridge ___ in 1990.", "options": ["was built", "is built", "has been built", "built"], "answer": "was built"},
            {"question": "She ___ be at home — the lights are on.", "options": ["can", "must", "shall", "will"], "answer": "must"},
            {"question": "He told me he ___ the project.", "options": ["finish", "finished", "had finished", "will finish"], "answer": "had finished"},
        ]
    },
    "B2": {
        "name": "🟠 B2 — Upper Intermediate",
        "emoji": "🟠",
        "questions_count": 10,
        "questions": [
            {"question": "If I ___ you, I would apologize.", "options": ["am", "was", "were", "had been"], "answer": "were"},
            {"question": "It's high time you ___ a decision.", "options": ["make", "made", "will make", "have made"], "answer": "made"},
            {"question": "I'd rather you ___ tell anyone about this.", "options": ["don't", "didn't", "won't", "hadn't"], "answer": "didn't"},
            {"question": "No sooner ___ he left than it started raining.", "options": ["did", "had", "was", "has"], "answer": "had"},
            {"question": "She ___ be tired — she's been working all day.", "options": ["can", "must", "shall", "will"], "answer": "must"},
            {"question": "Had she studied harder, she ___ the exam.", "options": ["pass", "passed", "would pass", "would have passed"], "answer": "would have passed"},
            {"question": "Not only ___ late, but he also forgot his report.", "options": ["he was", "was he", "he is", "is he"], "answer": "was he"},
            {"question": "He suggested that she ___ a doctor.", "options": ["see", "sees", "saw", "had seen"], "answer": "see"},
            {"question": "The painting ___ to be a forgery.", "options": ["proved", "was proved", "turned out", "was turning"], "answer": "turned out"},
            {"question": "Little ___ that his life was about to change.", "options": ["he knew", "did he know", "he had known", "had he known"], "answer": "did he know"},
        ]
    },
    "C1": {
        "name": "🔴 C1 — Advanced",
        "emoji": "🔴",
        "questions_count": 10,
        "questions": [
            {"question": "Seldom ___ such dedication in a student.", "options": ["I have seen", "have I seen", "I saw", "did I see"], "answer": "have I seen"},
            {"question": "It is essential that every student ___ on time.", "options": ["is", "are", "be", "will be"], "answer": "be"},
            {"question": "The suspect is alleged ___ the building at midnight.", "options": ["to enter", "to have entered", "entering", "having entered"], "answer": "to have entered"},
            {"question": "Were it not for her help, we ___ the project.", "options": ["won't complete", "wouldn't complete", "wouldn't have completed", "hadn't completed"], "answer": "wouldn't have completed"},
            {"question": "Under no circumstances ___ to negotiate.", "options": ["we should agree", "should we agree", "we agreed", "did we agree"], "answer": "should we agree"},
            {"question": "It is imperative that the data ___ before publication.", "options": ["verifies", "is verified", "be verified", "was verified"], "answer": "be verified"},
            {"question": "The accused denied ___ near the scene.", "options": ["to be", "being", "to have been", "having been"], "answer": "having been"},
            {"question": "Such was the noise ___ we couldn't hear each other.", "options": ["that", "which", "so", "as"], "answer": "that"},
            {"question": "Scarcely ___ when the alarm sounded.", "options": ["we had arrived", "had we arrived", "we arrived", "did we arrive"], "answer": "had we arrived"},
            {"question": "At no time ___ that the situation was critical.", "options": ["he admitted", "did he admit", "he had admitted", "had he admitted"], "answer": "did he admit"},
        ]
    },
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
        message.text = LEVELS[user_data[message.chat.id]["last_level"]]["name"]
        user_data[message.chat.id]["state"] = "choosing_level"
        choose_level(message)
    else:
        start(message)

if __name__ == "__main__":
    print("🚀 Bot ishga tushdi...")
    bot.infinity_polling()
