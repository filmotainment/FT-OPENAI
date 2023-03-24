import os
import openai
from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.types import Message

# Load environment variables from config.py file
from config import TELEGRAM_API_TOKEN, OPENAI_API_KEY, OPENAI_MODEL_ID, MONGODB_URI, \
                   PYROGRAM_API_ID, PYROGRAM_API_HASH, PYROGRAM_SESSION_NAME

# Connect to MongoDB database (optional)
if MONGODB_URI:
    db_client = MongoClient(MONGODB_URI)
    db = db_client.get_default_database()

# Connect to OpenAI API
openai.api_key = OPENAI_API_KEY


# Define Pyrogram bot client
app = Client(PYROGRAM_SESSION_NAME, api_id=PYROGRAM_API_ID, api_hash=PYROGRAM_API_HASH, bot_token=TELEGRAM_API_TOKEN)


# Handle '/start' command
@app.on_message(filters.command('start'))
def start_command_handler(client: Client, message: Message):
    """Sends a welcome message when the /start command is issued."""
    message.reply_text('Hi! I am an OpenAI-powered chatbot. Try sending me a message to get started!')


# Handle '/openai' command
@app.on_message(filters.command('openai'))
def openai_command_handler(client: Client, message: Message):
    """Generates a response using OpenAI's GPT-3 API."""
    # Extract the user input from the message
    user_input = message.text.replace('/openai', '').strip()

    # Generate a response using OpenAI's GPT-3 API
    response = openai.Completion.create(
        engine=OPENAI_MODEL_ID,
        prompt=user_input,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated response from the API response
    generated_text = response.choices[0].text.strip()

    # Send the generated response back to the user
    message.reply_text(generated_text)


# Handle incoming messages
@app.on_message(filters.text)
def message_handler(client: Client, message: Message):
    """Handles incoming messages by generating a response using OpenAI's GPT-3 API."""
    # Check if the message was sent by the bot itself
    if message.from_user.is_bot:
        return

    # Check if the user has interacted with the bot before (optional)
    if MONGODB_URI:
        user_data = db.user_data.find_one({'user_id': message.from_user.id})
        if user_data is None:
            db.user_data.insert_one({'user_id': message.from_user.id, 'context': ''})

    # Generate a response using OpenAI's GPT-3 API
    response = openai.Completion.create(
        engine=OPENAI_MODEL_ID,
        prompt=message.text,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated response from the API response
    generated_text = response.choices[0].text.strip()

    # Send the generated response back to the user
    message.reply_text(generated_text)


# Start the bot
app.run()
