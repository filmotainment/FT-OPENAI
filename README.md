# OpenAI Telegram Bot
This is a Telegram bot powered by OpenAI's GPT-3 API. The bot can generate human-like responses to messages sent to it.
## Usage
To use the bot, send a message to the bot and it will respond with a human-like message. You can also use the `/openai` command to generate a response to a specific prompt.
## Commands
• `/start` - Start the bot

• `/help` - Get help

• `/openai [prompt]` - Generate a response to the given prompt using OpenAI's GPT-3 API.
## Installation
To run the bot, follow these steps:
1. Clone this repository
2. Install the required dependencies with `pip install -r requirements.txt`
3. Set the environment variables in `.env`
4. Run the bot with `python bot.py`
## Environment Variables
• `TELEGRAM_BOT_TOKEN` - The API token for your Telegram bot

• `OPENAI_API_KEY` - Your OpenAI API key

• `MONGODB_URI` - The URI for your MongoDB database

• `MONGODB_NAME` - The name of the MongoDB database to use
## Deploying on Koyeb
You can deploy this bot on Koyeb by clicking the button below:

[![Deploy on Koyeb](https://deploy.koyeb.com/button.svg)](https://deploy.koyeb.com/deploy?source=https://github.com/filmotainment/FT-OPENAI)

