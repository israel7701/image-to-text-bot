import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.utils import executor
import pytesseract
from PIL import Image
import aiohttp
import io
import os

API_TOKEN = "7794084023:AAGd8Zw1cZp1KGHeS8JoiQeDP47k2kirrVs"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=ContentType.PHOTO)
async def handle_photo(message: types.Message):
    photo = message.photo[-1]
    photo_bytes = await photo.download(destination=io.BytesIO())
    photo_bytes.seek(0)
    image = Image.open(photo_bytes)
    text = pytesseract.image_to_string(image, lang='eng')
    await message.reply(f"📃 הטקסט שבתמונה:\n{text.strip() or 'לא זוהה טקסט.'}")

@dp.message_handler()
async def handle_text(message: types.Message):
    await message.reply("שלח לי תמונה ואני אזהה את הטקסט שבתוכה!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
