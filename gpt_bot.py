import os
import requests
import json
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Load environment variables from .env file
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GPT_API_KEY = os.getenv('GPT_API_KEY')

API_URL = os.getenv('API_URL')
TELEGRAM_MAX_MESSAGE_LENGTH = int(os.getenv('TELEGRAM_MAX_MESSAGE_LENGTH'))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! I am here to answer your questions about Chaining.",
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    # Send 'typing...' action
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(1)  # Introduce a short delay to make the typing action visible

    headers = {
        'Authorization': f'Bearer {GPT_API_KEY}',
        'Content-Type': 'application/json'
    }

    payload = {
        "chatId": "abcd",
        "stream": False,
        "detail": True,
        "variables": {
            "uid": "asdfadsfasfd2323",
            "name": "User"
        },
        "messages": [
            {
                "content": user_message,
                "role": "user"
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    response_data = response.json()
    # Add debug logging to inspect the response
    print(f"Response Data: {json.dumps(response_data, indent=2)}")

    if response_data and 'choices' in response_data and response_data['choices']:
        choice = response_data['choices'][0]
        content = None
        # Ensure 'message' is treated as a dictionary
        message_content = choice.get('message', {}).get('content', [])
        if isinstance(message_content, list):
        # Traverse the nested structure to find the content under text:content
            for message in choice['message']['content']:
                if message['type'] == 'text':
                    content = message['text']['content']
                    break

        if content:
            # Split the response into smaller parts if it exceeds the Telegram message length limit
            for part in split_text(content, TELEGRAM_MAX_MESSAGE_LENGTH):
                await update.message.reply_text(part)
        else:
            await update.message.reply_text("Sorry, I couldn't find the content in the response.")

    else:
        await update.message.reply_text("Sorry, I couldn't get a response from GPT.")

def split_text(text, max_length):
    """Splits text into chunks of max_length."""
    # Splitting text by sentences to ensure readability
    parts = []
    while len(text) > max_length:
        split_at = text[:max_length].rfind('. ')
        if split_at == -1:
            split_at = max_length
        parts.append(text[:split_at+1])
        text = text[split_at+1:]
    parts.append(text)
    return parts

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"Update {update} caused error {context.error}")

def run_bot() -> None:
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # on errors - print to the console
    application.add_error_handler(error_handler)

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    application.run_polling()