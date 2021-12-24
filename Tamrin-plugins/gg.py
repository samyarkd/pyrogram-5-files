from pyrogram import *
from googlesearch import search
from urltitle import URLTitleReader
from bing_image_urls import bing_image_urls
import urllib.request
import asyncio
import random

reader = URLTitleReader(verify_ssl=True)


@Client.on_message(filters.text, group = 4)
async def gg(client, message):
    text = message.text
    if text.startswith('/gg '):
        text = text.replace('/gg ', '')


        async def tiny_url(url):
            apiurl = "http://tinyurl.com/api-create.php?url="
            tinyurl = urllib.request.urlopen(apiurl + url).read()
            return tinyurl.decode("utf-8")

        srch = search(text)
        l1 = await tiny_url(srch[0])
        l2 = await tiny_url(srch[2])
        l3 = await tiny_url(srch[4])

        urls = bing_image_urls(text, limit=5)
        urls2 =[]
        for url in urls:
            try:
                await client.send_photo(chat_id='imgssssssssss', photo= url)
                urls2.append(url)
                        
            except Exception as e:
                pass
        urls = urls[random.randint(0,4)]
        srch = [reader.title(l1), reader.title(l2), reader.title(l3)]
        rn = '''
        3 نتیجه اول گوگل:

        1 . %s
           لینک : %s

        2 . %s
           لینک : %s

        3 . %s
           لینک : %s

             🕵  ️:  %s
        ''' %(srch[0],l1,srch[1],l2,srch[2],l3,text)           
        await client.send_photo(message.chat.id, photo=urls, caption = rn)

