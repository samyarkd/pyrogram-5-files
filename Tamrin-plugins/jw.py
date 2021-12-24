from pyrogram import *
import asyncio
import random

@Client.on_message(filters.text, group = 5)
async def jw(client, message):
    annss = {
        'باش': 'باش :) #%# بیا بخورش بیا  #%# 💋',
        'غلام': 'جانم چی میخوای',

    }

    if message.text in annss:
        if message.text == 'باش':
            st = annss[message.text]
            
            st = st.split('#%#')
            st = st[random.randint(0,2)]
            await message.reply(st)
        elif message.text != 'باش':
            try:
                await message.reply(annss[message.text])
                
            except Exception as e:
                pass
