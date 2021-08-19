from .constants import TELEGRAM_API_TOKEN, BOT_USERNAME, WEBHOOK_URL
from flask import Flask, request
import telegram, re, sqlite3
# from db import initDB, getAvailableItems, getPrice

global bot
global TOKEN
TOKEN = TELEGRAM_API_TOKEN
# bot = telegram.Bot(token = TOKEN)

app = Flask(__name__)

# @app.route('/{}'.format(TOKEN), methods = ['POST'])
# def respond():
#     update = telegram.Update.de_json(request.get_json(force=True), bot)
#     if update.message is None or update.message.text is None:
#         return 'ok'
#     chat_id = update.message.chat.id
#     msg_id = update.message.message_id

#     text = update.message.text.encode('utf-8').decode()

#     if re.match('^(?:/start|/help)$', text):
#         resp = """Welcome to our awesome grocery bot, Here's a list of available commands: \n\n- `/price <item>`: check the price of the given `<item>`\n\n- `/list`: returns a list of all available items in the store\n\n- `/help` or `/start`: returns this help message"""
#         bot.sendMessage(chat_id = chat_id, text = resp, parse_mode='Markdown', reply_to_message_id = msg_id)

#     elif re.match('^/list$', text):
#         try:
#             resp = getAvailableItems()
#         except:
#             resp = 'an error occured'
#         bot.sendMessage(chat_id = chat_id, text = resp, parse_mode='Markdown', reply_to_message_id = msg_id)

#     elif re.match('^/price .+$', text):
#         item = re.findall('^/price (.+)$', text)[0]
#         try:
#             resp = getPrice(item)
#         except:
#             resp = 'an error occured'
#         bot.sendMessage(chat_id = chat_id, text = resp, parse_mode='Markdown', reply_to_message_id = msg_id)

#     else:
#         bot.sendMessage(chat_id = chat_id, text = 'Wrong command :((', reply_to_message_id = msg_id)

#     return 'ok'


# @app.route('/set_webhook', methods=['GET', 'POST'])
# def set_webhook():
#    s = bot.setWebhook('{URL}{HOOK}'.format(URL=WEBHOOK_URL, HOOK=TOKEN))
#    if s:
#        return "webhook setup ok"
#    else:
#        return "webhook setup failed"

# @app.route('/initDB', methods=['GET'])
# def initdb():
#     try:
#         initDB()
#         return 'success'
#     except:
#         return 'error'

    
@app.route('/')
def index():
   return '.'

if __name__ == '__main__':
   app.run()
