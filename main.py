from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8743764310:AAEMf60TbwvipGC9N6f2xRFgWvPdDZb7j0I"


# ====== Commands =======

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 INFO-REXE-BOT Activated!\n"
        "Menu Ready:\n"
        "[ OSINT ]\n[ Crypto ]\n[ Tools ]\n[ Generate ]\n[ Owner ]"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Available Commands:\n"
        "/start – Start Bot\n"
        "/help – Help Menu\n"
        "/osint – OSINT Tools\n"
        "/crypto – Crypto Tools\n"
        "/tools – Tools Section\n"
        "/generate – Generate Tools\n"
        "/owner – Owner Info"
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


# ====== Application ======

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("osint", osint))
app.add_handler(CommandHandler("crypto", crypto))
app.add_handler(CommandHandler("tools", tools))
app.add_handler(CommandHandler("generate", generate))
app.add_handler(CommandHandler("owner", owner))

# Run Bot
app.run_polling()
