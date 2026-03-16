import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN
from utils.osint import osint_menu
from utils.crypto import crypto_menu
from utils.tools import tools_menu
from utils.generate import generate_menu
from utils.owner import owner_menu

logging.basicConfig(level=logging.INFO)

# ---------- START COMMAND ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔍 OSINT", callback_data="osint")],
        [InlineKeyboardButton("💰 Crypto", callback_data="crypto")],
        [InlineKeyboardButton("🛠 Tools", callback_data="tools")],
        [InlineKeyboardButton("⚡ Generate", callback_data="generate")],
        [InlineKeyboardButton("👑 Owner", callback_data="owner")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 INFO-REXE-BOT Activated!\nChoose a category:",
        reply_markup=reply_markup
    )

# ---------- CALLBACK HANDLER ----------
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

    if data == "osint":
        await osint_menu(query)
    elif data == "crypto":
        await crypto_menu(query)
    elif data == "tools":
        await tools_menu(query)
    elif data == "generate":
        await generate_menu(query)
    elif data == "owner":
        await owner_menu(query)

    await query.answer()

# ---------- MAIN RUN ----------
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(callback_handler))

    print("Bot Running…")
    app.run_polling()

if __name__ == "__main__":
    main()
