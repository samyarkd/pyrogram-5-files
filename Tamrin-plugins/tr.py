from pyrogram import *
from deep_translator import MyMemoryTranslator
import asyncio

@Client.on_message(filters.text, group = 2)
async def tr(client, message):
    
    text = message.text
    if text.startswith('/tr '):
        text = text.replace('/tr ', '')
        tr = MyMemoryTranslator(source= 'en', target= 'fa')
        tr = tr.translate(text)
        await message.reply(tr)

@Client.on_message(filters.text, group=1)
async def trf(client, message):
    
    text = message.text
    if text.startswith('/trf '):
        text = text.replace('/trf ', '')
        trf = MyMemoryTranslator(source= 'fa', target= 'en')
        trf = trf.translate(text)
        await message.reply(trf)

@Client.on_message(filters.text, group=8)
async def trr(client, message):
    
    text = (message.text).lower()
    
    if (text.startswith('trr') or text.startswith('trf') or text.startswith('tr') or text.startswith('/trr') or text.startswith('/trf') or text.startswith('/tr') or text.startswith('/tr@samyarborderbot') or text.startswith("'/trr@samyarborderbot'") or text.startswith("'/trf@samyarborderbot'") ) and message.reply_to_message:
       
       
       trf = MyMemoryTranslator(source= 'en', target= 'fa')
       trf = trf.translate(message.reply_to_message.text)
       await message.reply(trf)
        
       tr= MyMemoryTranslator(source= 'fa', target= 'en')
       tr = tr.translate(message.reply_to_message.text)
       await message.reply(tr)
