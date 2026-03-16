# utils/owner.py
from config import OWNER_USERNAME, OWNER_ID

async def owner_menu(query):
    text = (
        "👑 *Owner Panel*\n"
        f"Username: {OWNER_USERNAME}\n"
        f"ID: `{OWNER_ID}`\n"
        "\nContact for:\n"
        "✔ Custom Bots\n"
        "✔ OSINT Panels\n"
        "✔ Paid APIs\n"
        "✔ Tools\n"
    )
    await query.edit_message_text(text, parse_mode="Markdown")
