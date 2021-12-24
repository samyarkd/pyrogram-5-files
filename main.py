from pyrogram import *

import api

api_id = api.api_key
api_hash = api.api_hash

bot_tok = '5065160661:AAEed5jVGPlHwpRzeH4C1v7p5t3u8rAfI5U'


plugins = dict(root='plugins')


app = Client('translate', api_id, api_hash, bot_token=bot_tok, plugins=plugins)


app.run()
