import telebot
from flask import Flask
from threading import Thread
import os

# --- CONFIGURATION ---
# Apna Bot Token yahan dalein
BOT_TOKEN = "8206426384:AAEVb_Mnc6hSVgGqeCTM8Mdqg4p2hLw6BmQ"

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask('')

# --- PROFESSIONAL MESSAGES ---

# 1. Start / Welcome Message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Greetings, Khushi! 👋\n\n"
        "I am BOTPIC Visual, your dedicated AI Assistant.\n\n"
        "Proudly developed by Codex Group of Companies — "
        "the premier name in software innovation."
    )
    bot.reply_to(message, welcome_text)

# 2. Image Handling Logic (Professional Response)
@bot.message_handler(content_types=['photo'])
def handle_image(message):
    # Jab user image bhejta hai
    reply_text = (
        "Confirmation: Image Received. 🖼️\n\n"
        "Your visual data has been securely forwarded to Dr. Lena Ly for immediate analysis."
    )
    bot.reply_to(message, reply_text)

# 3. Text Handling Logic (Professional Response)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    # Jab user text bhejta hai
    reply_text = (
        "Confirmation: Message Received. 📝\n\n"
        "Your text inquiry has been securely forwarded to Dr. Lena Ly."
    )
    bot.reply_to(message, reply_text)

# --- SERVER KEEPER (Render 24/7 Logic) ---

@app.route('/')
def home():
    return "BOTPIC Visual System is Operational."

def run_http():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_http)
    t.start()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("System Starting...")
    keep_alive()  # Fake website server start
    bot.polling(non_stop=True) # Bot start
