import os
import logging
import threading
from flask import Flask, request
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Load API keys from environment variables
TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask
app = Flask(__name__)

# Function to handle user messages
def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text
    response = f"Received: {user_text}"  # Replace with AI-generated response if needed
    update.message.reply_text(response)

# Function to start the bot
def run_bot():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

# Run the bot in a separate thread so Flask can run too
threading.Thread(target=run_bot).start()

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
