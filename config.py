import os

# Telegram Bot API token
TELEGRAM_API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN')

# OpenAI API key
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# OpenAI language model ID
OPENAI_MODEL_ID = os.environ.get('OPENAI_MODEL_ID')

# MongoDB URI for user data storage (optional)
MONGODB_URI = os.environ.get('MONGODB_URI')

# Pyrogram API ID and API hash
PYROGRAM_API_ID = os.environ.get('PYROGRAM_API_ID')
PYROGRAM_API_HASH = os.environ.get('PYROGRAM_API_HASH')

# Pyrogram bot session name
PYROGRAM_SESSION_NAME = os.environ.get('PYROGRAM_SESSION_NAME')

PORT = int(os.environ.get('PORT', 8080))

