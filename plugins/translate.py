from deep_translator import GoogleTranslator
from pyrogram import Client, filters


@Client.on_message(filters.private & filters.text, group=1)
async def translate(c, m):
    # مترجم ساختن
    translator = GoogleTranslator('auto', 'fa')
    translator_to_en = GoogleTranslator('auto', 'en')
    # ترجمه متن
    translated = translator.translate(m.text)
    translated_to_en = translator_to_en.translate(m.text)
    # ارسال ترجمه شده
    await m.reply_text(translated)
    await m.reply_text(translated_to_en)

# /tr_en hello
# سلام

# /tr_fa سلام
# hello

