from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

TOKEN = "8743764310:AAEMf60TbwvipGC9N6f2xRFgWvPdDZb7j0I"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 INFO-REXE-BOT Activated!\n"
        "[ OSINT ]\n[ Crypto ]\n[ Tools ]\n[ Generate ]\n[ Owner ]"
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Commands:\n/start\n/help\n/osint\n/crypto\n/tools\n/generate\n/owner"
    )


async def osint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 OSINT Tools Loading…")


async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 Crypto Tools Soon…")


async def tools(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛠 Tools Loading…")


async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚙️ Generator Tools Coming…")


async def owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👑 Owner: @Cyberrexetools_bot")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("osint", osint))
app.add_handler(CommandHandler("crypto", crypto))
app.add_handler(CommandHandler("tools", tools))
app.add_handler(CommandHandler("generate", generate))
app.add_handler(CommandHandler("owner", owner))

app.run_polling()
