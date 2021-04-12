from dotenv import load_dotenv
import urllib.request
import requests
import json
import os

load_dotenv()
LUNACRUSH_API_KEY = os.environ.get("LUNACRUSH_API_KEY")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Aca van los comandos que tiene el bot")

def get_coin_info(coin_symbol):
    url = f"https://api.lunarcrush.com/v2?data=assets&key={LUNACRUSH_API_KEY}&symbol={coin_symbol}"
    coin_info = requests.get(url).json()
    return coin_info

def get_coin_price(coin_symbol):
    coin_info = get_coin_info(coin_symbol)
    return {"price": coin_info["data"][0]["price"]}

def get_coin_change(coin_symbol, change_period='24h'):
    coin_info = get_coin_info(coin_symbol)
    data = coin_info["data"][0]
    percent_change_key = f"percent_change_{change_period}"
    if percent_change_key not in data.keys():
        return {}
    return {percent_change_key: f"{data[percent_change_key]}%"}

def price(update, context):
    coin =  context.args[0].upper()
    data = get_coin_price(coin)
    extra_data = {}
    if len(context.args) > 1:
        change_period = context.args[1]
        extra_data = {**extra_data, **get_coin_change(coin, change_period)}
    msg = f"Precio del {coin}: {str(data['price'])} USD"
    for k, v in extra_data.items():
        msg = f"{msg} \n --> {k} : {v}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)