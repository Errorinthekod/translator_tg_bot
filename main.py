from aiogram import Bot, types, Dispatcher, executor
from translator import translator#, translator_kz
from config_token import TOKEN
from aiogram.types import Message

token = TOKEN
bot = Bot(token)
dp = Dispatcher(bot)

    
@dp.message_handler(content_types='text')
async def translate_en(msg: types.Message):
    text = translator(text=msg.text)
    await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
    await msg.answer(text)
  
    
# @dp.message_handler(content_types='text')
# async def translate_kz(msg: types.Message):
#     text = translator_kz(text=msg.text)
#     await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
#     await msg.answer(text)

if __name__ == '__main__':
    executor.start_polling(dp)
