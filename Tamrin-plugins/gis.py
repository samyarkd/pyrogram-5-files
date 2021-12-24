from bing_image_urls import bing_image_urls
import asyncio
from pyrogram import *
from pyrogram.types import InputMediaPhoto, InputMediaVideo





@Client.on_message(filters.text, group = 0)
async def gisi(client, message):
    
    async def sdas():
        text = message.text
        if text.startswith('/gis '):
            text = text.replace('/gis ', '')
            # await message.reply(text)
            urls = bing_image_urls(text, limit=10)
            urls2 =[]
            for url in urls:
                try:
                    await client.send_photo(chat_id='imgssssssssss', photo= url)
                    urls2.append(InputMediaPhoto(url, caption=text))
                    
                except Exception as e:
                    pass
            await client.send_media_group(
            message.chat.id, urls2)
    
    if message.chat.type == 'private':
        await sdas()
    else:
        mms = await client.get_chat_member(message.chat.id, message.from_user.id)    
        mms = mms.status
        mmid = message.from_user.id
        if mms == 'member' and mmid != 748891997 and mmid != 1864394667:
            text = message.text
            if text.startswith('/gis '):
                text = text.replace('/gis ', '')
                await message.reply('این دستور برای ادمین های گروه کار میکنه فقط میتونی بیای پی 😙')
        else:
            await sdas()
