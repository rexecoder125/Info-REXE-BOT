# utils/crypto.py
import requests

async def crypto_menu(query):
    text = "💰 *Crypto Tools*\nSelect:"
    await query.edit_message_text(text, parse_mode="Markdown")


# Live BTC Price
def btc_price():
    return requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()


# Live ETH Price
def eth_price():
    return requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot").json()
