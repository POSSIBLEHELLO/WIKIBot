# import logging
# 
# from aiogram import Bot, Dispatcher, executor, types
# from search_wiki import get_wiki_page
# 
# API_TOKEN = '6082663790:AAEqFqwLSIl3kqEZ12d0SFMCqEuIZBoDBs4'
# 
# 
# logging.basicConfig(level=logging.INFO)
# 
# 
# 
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
# 
# menu_btn = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# menu_btn.add(
    # types.KeyboardButton("Photo"),
    # types.KeyboardButton("Audio"),
    # types.KeyboardButton("Video"),
# )
#    
# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
    # await message.answer("Hi!", reply_markup=menu_btn)
# 
# @dp.message_handler(text=['Hello'])
# async def send_welcome2(message: types.Message):
    # await message.answer("Valeykum ukam.")
# 
# @dp.message_handler()
# async def echo(message: types.Message):
    #  text = message.text
    #  if text == "Goodbye":
        #  await message.answer("Yaxshi dam oling")
    #  elif text == "Video":
        #  video = types.InputFile("mp4.mp4")                                                                               
        #  await message.answer_video(video = video)
    #  elif text == "Photo":
        #  photo = types.InputFile("nature.jpg")
        #  await message.answer_photo(photo=photo)
    #  elif text == "Audio":
        #  audio = types.InputFile("Eminem_-_Mockingbird.mp3")
        #  await message.answer_audio(audio=audio)
    #  else:
        #  await message.answer(message.text)
# 
# 
# 
# @dp.message_handler(regexp='[a-z]')
# async def send_welcome3(message: types.Message):
    # await message.answer("Bo'pti")
# 
# @dp.message_handler(content_types=['text'])
# async def user_text_handle(message: types.Message):
#    uesr_text = message.text
#    result = get_wiki_page(uesr_text)
#    await message.answer(result)
# 
# text, video, document, photo, animation, sticker, voice, audio
# if __name__ == '__main__':
#  executor.start_polling(dp, skip_updates=True)
# 
# 