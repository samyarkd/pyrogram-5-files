from pyrogram import *
from bing_image_urls import bing_image_urls
import asyncio
import wikipedia
import random

@Client.on_message(filters.text, group = 3)
async def wiki(client, message):
    text = message.text
    if text.startswith('/wiki '):
        wikipedia.set_lang("fa")
        text = text.replace('/wiki ', '')
        wk = wikipedia.summary(text, sentences=5)

        urls = bing_image_urls(text, limit=5)
        urls2 =[]
        for url in urls:
            try:
                await client.send_photo(chat_id='imgssssssssss', photo= url)
                urls2.append(url)
                    
            except Exception as e:
                print(e)
        print(urls2)

        try:
            url = urls2[random.randint(0,4)]
        except:
            try:
                url = urls2[0]
            except:
                url = 'https://r2gate.org/wp-content/uploads/2019/12/image.png'
        if message.chat.type == 'private':
            pass
        else: 
            wk = wk + '\n \n 📒 ادامه مطلب رو در پی وی بخون'
        
        await client.send_photo(message.chat.id, photo=url, caption = wk)
        
        if message.chat.type == 'private':
            wk1 = wikipedia.page(text)
            wk1 = wk1.content
            n = 4000 
            chunks = [wk1[i:i+n] for i in range(0, len(wk1), n)]
            
            for text in chunks:
                await client.send_message(message.chat.id, text)
