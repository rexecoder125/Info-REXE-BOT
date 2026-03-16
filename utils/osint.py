# utils/osint.py
import requests

async def osint_menu(query):
    text = "🔍 *OSINT Tools Menu*\nChoose a tool:"
    await query.edit_message_text(text, parse_mode="Markdown")


# IP Lookup
async def ip_lookup(ip):
    return requests.get(f"http://ip-api.com/json/{ip}").json()


# Email Lookup (Free API)
async def email_lookup(email):
    return requests.get(f"https://api.eva.pingutil.com/email?email={email}").json()


# Username Lookup
async def username_lookup(username):
    return {
        "instagram": f"https://instagram.com/{username}",
        "github": f"https://github.com/{username}",
        "twitter": f"https://twitter.com/{username}",
        "tiktok": f"https://tiktok.com/@{username}"
    }
