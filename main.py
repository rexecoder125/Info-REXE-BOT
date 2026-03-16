from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

TOKEN = "8743764310:AAEMf60TbwvipGC9N6f2xRFgWvPdDZb7j0I"


# ==========================
#        COMMANDS
# ==========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 INFO-REXE-BOT Activated!\n"
        "Menu Ready:\n"
        "[ OSINT ]\n[ Crypto ]\n[ Tools ]\n[ Generate ]\n[ Owner ]"
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Commands List:\n"
        "/start\n/help\n/osint\n/crypto\n/tools\n/generate\n/owner"
    )


async def osint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 OSINT Tools Loading…")


async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 Crypto Scanner Coming…")


async def tools(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛠 Tools Coming Soon…")


async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚙️ Generator Tools Loading…")


async def owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👑 Owner: @Cyberrexetools_bot")


# ==========================
#     BOT APPLICATION
# ==========================

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("osint", osint))
app.add_handler(CommandHandler("crypto", crypto))
app.add_handler(CommandHandler("tools", tools))
app.add_handler(CommandHandler("generate", generate))
app.add_handler(CommandHandler("owner", owner))

app.run_polling()
