import logging
import re
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

TOKEN =os.getenv('TOKEN') 
bot = Bot(token= TOKEN)
dp = Dispatcher(bot=bot)
logging.basicConfig(level= logging.INFO, filename = 'mylog.log')

@dp.message(Command(commands=['start']))
async def greetings_user(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! напиши свое ФИО'
    logging.info(f'Этот пользователь {user_name}, с ИД {user_id} запустил бота')
    await bot.send_message(chat_id= user_id, text=text)
    
slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh',
      'ц':'ts','ч':'ch','ш':'sh','щ':'shch','ъ':'ie','ы':'y','ь':'','э':'e',
      'ю':'iu','я':'ia','А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'E',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'KH',
      'Ц':'TS','Ч':'CH','Ш':'SH','Щ':'SHCH','Ъ':'IE','Ы':'y','Ь':'','Э':'E',
      'Ю':'IU','Я':'IA',',':'','?':'',' ':'_','~':'','!':'','@':'','#':'',
      '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
      ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
      '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
      'Є':'e', '—':''}
def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))

@dp.message()
async def send_message(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    if has_cyrillic(text):
        res = "".join([slovar[i].upper() for i in text])
    else:
        res = 'Бот принимает только текст на кириллице, введите корректный текст'
    logging.info(f'Этот пользователь {user_name}, с ИД {user_id} отправил {text}')
    await message.answer(text = res )
    
if __name__ == '__main__':
    dp.run_polling(bot)
    
