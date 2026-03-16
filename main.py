import logging
import requests
import random, string
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ==========================
TOKEN = "8743764310:AAEMf60TbwvipGC9N6f2xRFgWvPdDZb7j0I"
OWNER_ID = 7027444755
# ==========================

MAIN_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("🕵️ OSINT", callback_data="osint_menu")],
    [InlineKeyboardButton("💰 Crypto", callback_data="crypto_menu")],
    [InlineKeyboardButton("🛠 Tools", callback_data="tools_menu")],
    [InlineKeyboardButton("⚡ Generate", callback_data="gen_menu")],
    [InlineKeyboardButton("👑 Owner", callback_data="owner_menu")]
])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 INFO-REXE BOT Online!\nSelect Category:",
        reply_markup=MAIN_MENU
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    d = q.data

    if d == "osint_menu":
        await q.edit_message_text(
            "🕵️ OSINT Tools:\n\n"
            "/ip <ip>\n/user <username>\n/whois <domain>\n/instainfo <username>",
            reply_markup=MAIN_MENU
        )

    elif d == "crypto_menu":
        await q.edit_message_text(
            "💰 CRYPTO MENU:\n\n/btc\n/eth\n/doge",
            reply_markup=MAIN_MENU
        )

    elif d == "tools_menu":
        await q.edit_message_text(
            "🛠 TOOLS:\n\n/bin <bin>\n/qrcode <text>\n/fake\n/pwd",
            reply_markup=MAIN_MENU
        )

    elif d == "gen_menu":
        await q.edit_message_text(
            "⚡ GENERATE:\n\n/pass\n/fake\n",
            reply_markup=MAIN_MENU
        )

    elif d == "owner_menu":
        await q.edit_message_text(
            "👑 OWNER PANEL:\n/stats\n/broadcast <msg>",
            reply_markup=MAIN_MENU
        )


# ------ OSINT ------
async def ip_lookup(update, context):
    if not context.args:
        return await update.message.reply_text("Usage: /ip 1.1.1.1")

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


async def user_osint(update, context):
    if not context.args:
        return await update.message.reply_text("Usage: /user username")

    u = context.args[0]
    r = requests.get(f"https://api.github.com/users/{u}").json()

    msg = f"""
🕵️ USER OSINT
User: {u}
Name: {r.get("name")}
Bio: {r.get("bio")}
Followers: {r.get("followers")}
Repos: {r.get("public_repos")}
Profile: {r.get("html_url")}
"""
    await update.message.reply_text(msg)


async def whois(update, context):
    if not context.args:
        return await update.message.reply_text("Use: /whois example.com")
    d = context.args[0]
    r = requests.get(f"https://api.hackertarget.com/whois/?q={d}").text
    await update.message.reply_text(r)


async def instainfo(update, context):
    if not context.args:
        return await update.message.reply_text("Use: /instainfo username")

    user = context.args[0]
    url = f"https://www.instagram.com/{user}/?__a=1&__d=dis"

    try:
        r = requests.get(url).json()
        u = r["graphql"]["user"]

        msg = f"""
📸 *Instagram Info*
User: {user}
Name: {u["full_name"]}
Followers: {u["edge_followed_by"]["count"]}
Following: {u["edge_follow"]["count"]}
"""
    except:
        msg = "❌ Not Found or Private"

    await update.message.reply_text(msg, parse_mode="Markdown")


# ------ CRYPTO ------
async def btc(update, context):
    p = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json").json()["bpi"]["USD"]["rate"]
    await update.message.reply_text(f"₿ BTC: ${p}")

async def eth(update, context):
    p = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot").json()["data"]["amount"]
    await update.message.reply_text(f"Ξ ETH: ${p}")

async def doge(update, context):
    p = requests.get("https://api.coinbase.com/v2/prices/DOGE-USD/spot").json()["data"]["amount"]
    await update.message.reply_text(f"🐶 DOGE: ${p}")


# ------ TOOLS ------
async def bin_lookup(update, context):
    if not context.args:
        return await update.message.reply_text("Use: /bin 457173")

    b = context.args[0]
    r = requests.get(f"https://lookup.binlist.net/{b}").json()

    msg = f"""
💳 *BIN Lookup*
Bank: {r['bank']['name']}
Country: {r['country']['name']}
Type: {r['type']}
Scheme: {r['scheme']}
"""
    await update.message.reply_text(msg, parse_mode="Markdown")


async def fake(update, context):
    r = requests.get("https://randomuser.me/api/").json()['results'][0]

    msg = f"""
🧪 Fake Info
Name: {r['name']['first']} {r['name']['last']}
Email: {r['email']}
Phone: {r['phone']}
Country: {r['location']['country']}
"""
    await update.message.reply_text(msg)


async def pwd(update, context):
    chars = string.ascii_letters + string.digits
    ps = "".join(random.choice(chars) for _ in range(12))
    await update.message.reply_text(f"🔐 `{ps}`", parse_mode="Markdown")


async def qrcode(update, context):
    if not context.args:
        return await update.message.reply_text("Use: /qrcode text")
    t = " ".join(context.args)
    u = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={t}"
    await update.message.reply_photo(u)


# ------ OWNER ------
async def stats(update, context):
    if update.message.chat.id != OWNER_ID:
        return await update.message.reply_text("❌ Not Allowed")
    await update.message.reply_text("📊 Bot Running Perfectly.")


async def broadcast(update, context):
    if update.message.chat.id != OWNER_ID:
        return await update.message.reply_text("❌ Not Allowed")
    msg = " ".join(context.args)
    await update.message.reply_text("Broadcast Sent (Demo Mode)")


# ------ MAIN ------
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.add_handler(CommandHandler("ip", ip_lookup))
    app.add_handler(CommandHandler("user", user_osint))
    app.add_handler(CommandHandler("whois", whois))
    app.add_handler(CommandHandler("instainfo", instainfo))

    app.add_handler(CommandHandler("btc", btc))
    app.add_handler(CommandHandler("eth", eth))
    app.add_handler(CommandHandler("doge", doge))

    app.add_handler(CommandHandler("bin", bin_lookup))
    app.add_handler(CommandHandler("fake", fake))
    app.add_handler(CommandHandler("pwd", pwd))
    app.add_handler(CommandHandler("qrcode", qrcode))

    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("broadcast", broadcast))

    await app.run_polling()

import asyncio
asyncio.run(main())
