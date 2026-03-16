# utils/tools.py
import base64
import random
import string
import requests

async def tools_menu(query):
    text = "🛠 *Tools Menu*\nChoose:"
    await query.edit_message_text(text, parse_mode="Markdown")


def generate_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(12))


def base64_encode(text):
    return base64.b64encode(text.encode()).decode()


def base64_decode(text):
    return base64.b64decode(text.encode()).decode()


def qr_code(text):
    return f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={text}"
