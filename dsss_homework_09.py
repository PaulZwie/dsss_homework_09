from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /start command. Sends a welcome message to the user.

    Args:
        update (Update): Incoming update from Telegram.
        context (ContextTypes.DEFAULT_TYPE): Context object containing bot data.
    """
    await update.message.reply_text('Hello! I am your bot, ready to help you!')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle incoming text messages. Echoes the received message back to the user.

    Args:
        update (Update): Incoming update from Telegram.
        context (ContextTypes.DEFAULT_TYPE): Context object containing bot data.
    """
    received_text = update.message.text
    response = f"You: {received_text} "
    await update.message.reply_text(response)

async def send_message(context: ContextTypes.DEFAULT_TYPE, chat_id: int, text: str) -> None:
    """
    Send a message to a specific chat.

    Args:
        context (ContextTypes.DEFAULT_TYPE): Context object containing bot data.
        chat_id (int): ID of the chat to send the message to.
        text (str): Text of the message to send.
    """
    await context.bot.send_message(chat_id=chat_id, text=text)

def main():
    """
    Main function to start the bot. Sets up the command and message handlers and starts polling.
    """
    application = ApplicationBuilder().token("7964637326:AAHveuiwmcGx8ZkQbBB5DoQx6D2Rq1VugWU").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()