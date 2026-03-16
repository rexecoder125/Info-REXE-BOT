import logging
import requests
import random, string
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ==========================
TOKEN = "8743764310:AAEMf60TbwvipGC9N6f2xRFgWvPdDZb7j0I"
OWNER_ID = 7027444755
# ==========================

# ------------------------------
# Start Menu UI
# ------------------------------
MAIN_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("🕵️ OSINT", callback_data="osint_menu")],
    [InlineKeyboardButton("💰 Crypto", callback_data="crypto_menu")],
    [InlineKeyboardButton("🛠 Tools", callback_data="tools_menu")],
    [InlineKeyboardButton("⚡ Generate", callback_data="gen_menu")],
    [InlineKeyboardButton("👑 Owner", callback_data="owner_menu")]
])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 INFO-REXE BOT Online!\nSelect a category below:",
        reply_markup=MAIN_MENU
    )

# ------------------------------  
# MENU CALLBACKS
# ------------------------------
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    # OSINT Menu
    if data == "osint_menu":
        await query.edit_message_text(
            "🕵️ OSINT Tools:\n\n"
            "/ip <ip>\n"
            "/user <username>\n"
            "/whois <domain>\n"
            "/instainfo <username>",
            reply_markup=MAIN_MENU
        )

    # Crypto Menu
    elif data == "crypto_menu":
        await query.edit_message_text(
            "💰 Crypto Tools:\n\n"
            "/btc\n/eth\n/doge",
            reply_markup=MAIN_MENU
        )

    # Tools Menu
    elif data == "tools_menu":
        await query.edit_message_text(
            "🛠 Tools:\n\n"
            "/bin <bin>\n"
            "/qrcode <text>\n"
            "/fake\n"
            "/pwd",
            reply_markup=MAIN_MENU
        )

    # Generate Menu
    elif data == "gen_menu":
        await query.edit_message_text(
            "⚡ Generate Options:\n\n"
            "/pass\n/fake\n",
            reply_markup=MAIN_MENU
        )

    # Owner Menu
    elif data == "owner_menu":
        await query.edit_message_text(
            "👑 OWNER PANEL:\nOnly ReXe Can Use.\n\n"
            "/stats\n/broadcast <msg>",
            reply_markup=MAIN_MENU
        )

# ===================================================================
# 🔥 OSINT FUNCTIONS
# ===================================================================

# IP Lookup
async def ip_lookup(update, context):
    if not context.args:
        return await update.message.reply_text("Use: /ip 1.1.1.1")

    ip = context.args[0]
    r = requests.get(f"http://ip-api.com/json/{ip}").json()

    msg = f"""
🕵️ *IP Lookup*
IP: {ip}
Country: {r.get('country')}
City: {r.get('city')}
Region: {r.get('regionName')}
ISP: {r.get('isp')}
Status: {r.get('status')}
"""
    await update.message.reply_text(msg, parse_mode="Markdown")

# USER OSINT
async def user_osint(update, context):
    if not context.args:
        return await update.message.reply_text("Use: /user username")

    u = context.args[0]
    r = requests.get(f"https://api.github.com/users/{u}").json()

    msg = f"""
🕵️ *Username OSINT*
User: {u}
Name: {r.get("name")}
Bio: {r.get("bio")}
Followers: {r.get("followers")}
Public Repo: {r.get("public_repos")}
Profile: {r.get("html_url")}
"""
    await update.message.reply_text(msg)

# WHOIS
async def whois(update, context):
    if not context.args:
        return await update.message.reply_text("Use: /whois example.com")
    domain = context.args[0]
    r = requests.get(f"https://api.hackertarget.com/whois/?q={domain}").text
    await update.message.reply_text(r)

# Insta Info (Free)
async def instainfo(update, context):
    if not context.args:
        return await update.message.reply_text("Use: /instainfo username")

    user = context.args[0]
    url = f"https://www.instagram.com/{user}/?__a=1&__d=dis"
    
    try:
        r = requests.get(url).json()
        name = r["graphql"]["user"]["full_name"]
        followers = r["graphql"]["user"]["edge_followed_by"]["count"]
        following = r["graphql"]["user"]["edge_follow"]["count"]

        msg = f"""
📸 *Instagram Info*
User: {user}
Name: {name}
Followers: {followers}
Following: {following}
"""
    except:
        msg = "❌ Account Not Found / Private."

    await update.message.reply_text(msg, parse_mode="Markdown")

# ===================================================================
# 💰 CRYPTO PRICE API
# ===================================================================

async def btc(update, context):
    p = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json").json()["bpi"]["USD"]["rate"]
    await update.message.reply_text(f"₿ BTC Price: ${p}")

async def eth(update, context):
    p = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot").json()["data"]["amount"]
    await update.message.reply_text(f"Ξ ETH Price: ${p}")

async def doge(update, context):
    p = requests.get("https://api.coinbase.com/v2/prices/DOGE-USD/spot").json()["data"]["amount"]
    await update.message.reply_text(f"🐶 DOGE Price: ${p}")

# ===================================================================
# 🛠 TOOLS
# ===================================================================

# BIN Checker
async def bin_lookup(update, context):
    if not context.args:
        return await update.message.reply_text("Use: /bin 457173")

    bin_number = context.args[0]
    r = requests.get(f"https://lookup.binlist.net/{bin_number}").json()

    msg = f"""
💳 *BIN Lookup*

Bank: {r['bank']['name']}
Country: {r['country']['name']}
Scheme: {r['scheme']}
Type: {r['type']}
"""
    await update.message.reply_text(msg, parse_mode="Markdown")

# Fake Info
async def fake(update, context):
    r = requests.get("https://randomuser.me/api/").json()['results'][0]

    msg = f"""
🧪 *Fake Identity*
Name: {r['name']['first']} {r['name']['last']}
Email: {r['email']}
Phone: {r['phone']}
Country: {r['location']['country']}
"""
    await update.message.reply_text(msg, parse_mode="Markdown")

# Password Generate
async def pwd(update, context):
    chars = string.ascii_letters + string.digits
    ps = "".join(random.choice(chars) for _ in range(12))
    await update.message.reply_text(f"🔐 Password: `{ps}`", parse_mode="Markdown")

# QR Code
async def qrcode(update, context):
    if not context.args:
        return await update.message.reply_text("Use: /qrcode hello")
    text = " ".join(context.args)
    url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={text}"
    await update.message.reply_photo(url)

# ===================================================================
# 👑 OWNER FUNCTIONS
# ===================================================================

async def stats(update, context):
    if update.message.chat.id != OWNER_ID:
        return await update.message.reply_text("❌ Owner Only Access")
    await update.message.reply_text("📊 Bot Running Successfully.\nOwner: ReXe")

async def broadcast(update, context):
    if update.message.chat.id != OWNER_ID:
        return await update.message.reply_text("❌ Owner Only Access")
    msg = " ".join(context.args)
    await update.message.reply_text("Sent to All Users (Demo Mode).")

# ===================================================================
# MAIN BOT RUN
# ===================================================================

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    # OSINT
    app.add_handler(CommandHandler("ip", ip_lookup))
    app.add_handler(CommandHandler("user", user_osint))
    app.add_handler(CommandHandler("whois", whois))
    app.add_handler(CommandHandler("instainfo", instainfo))

    # Crypto
    app.add_handler(CommandHandler("btc", btc))
    app.add_handler(CommandHandler("eth", eth))
    app.add_handler(CommandHandler("doge", doge))

    # Tools
    app.add_handler(CommandHandler("bin", bin_lookup))
    app.add_handler(CommandHandler("fake", fake))
    app.add_handler(CommandHandler("pwd", pwd))
    app.add_handler(CommandHandler("qrcode", qrcode))

    # Owner
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("broadcast", broadcast))

    await app.run_polling()

# Run
import asyncio
asyncio.run(main())
