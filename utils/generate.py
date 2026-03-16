# utils/generate.py
import requests

async def generate_menu(query):
    text = "⚡ *Generate Tools*\nChoose:"
    await query.edit_message_text(text, parse_mode="Markdown")


def fake_profile():
    return requests.get("https://randomuser.me/api/").json()["results"][0]
