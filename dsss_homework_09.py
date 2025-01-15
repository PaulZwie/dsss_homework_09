import torch
import transformers
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

device = "cuda" if torch.cuda.is_available() else "cpu"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device=device,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    start command, to start the Bot

    Args:
        update (Update): Incoming update from Telegram.
        context (ContextTypes.DEFAULT_TYPE): Context object containing bot data.
    """
    await update.message.reply_text('Hello! I am your bot, ready to help you!')


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle incoming text messages, and returns the answer of the LLM

    Args:
        update (Update): Incoming update from Telegram.
        context (ContextTypes.DEFAULT_TYPE): Context object containing bot data.
    """
    input_message = update.message.text

    messages = [
        {"role": "user", "content": input_message}
    ]
    output = pipeline(messages, max_new_tokens=256)
    # print(output[0]["generated_text"])
    output = output[0]["generated_text"][1]['content']
    await update.message.reply_text(output)


async def send_message(context: ContextTypes.DEFAULT_TYPE, chat_id: int, text: str) -> None:
    """
    Sends the message to telegram

    Args:
        context (ContextTypes.DEFAULT_TYPE): Context object containing bot data.
        chat_id (int): ID of the chat to send the message to.
        text (str): Text of the message to send.
    """
    await context.bot.send_message(chat_id=chat_id, text=text)


def main():
    """
    Starts the Bot
    """
    application = ApplicationBuilder().token("7964637326:AAHveuiwmcGx8ZkQbBB5DoQx6D2Rq1VugWU").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


if __name__ == '__main__':
    main()
