import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = "8743764310:AAEMf60TbwvipGC9N6f2xRFgWvPdDZb7j0I"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 INFO-REXE-BOT Running Successfully on Heroku!\n\n"
        "Type /help to see available commands."
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 Available Commands:\n"
        "/start - Check Bot Status\n"
        "/help - Show this help message\n"
        "\nMore commands coming soon… 🔥"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))

    print("BOT RUNNING…")
    app.run_polling()

if __name__ == "__main__":
    main()
