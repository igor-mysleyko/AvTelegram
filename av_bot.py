import json
import time

from call import collect_data
from aiogram import Bot, Dispatcher,executor,types
from aiogram.dispatcher.filters import Text                    # фильтр текста
from aiogram.utils.markdown import hbold, hlink                # получение ссылок
import os

bot=Bot(token='5672994651:AAGbtwzKLbKOIznEJpccyrLlr0AgBoUo0bY', parse_mode=types.ParseMode.HTML)
dp= Dispatcher(bot)

@dp.message_handler(commands='start')          # Формирование клавиатуры
async def start(message: types.Message):
    start_button=['за последний час!!!', 'за два часа']       # объеденение кнопок
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)    #создание объекта клавиатуры\уменьшение кнопок
    keyboard.add(*start_button)                # добавление списка кнопок

    await message.answer('выберите категорию', reply_markup=keyboard)   # отсылка сообщения пользователю




@dp.message_handler(Text(equals='за последний час!!!'))      # хендлер за последний час, фильтр текста
async def get_call(message : types.Message):
    await message.answer("подождите...")

    collect_data()

    with open('args.json') as f:
        data=json.load(f)

    for index, item in enumerate(data):                                       # формируем карточку для вывода
        card = f'{hlink(item.get("link_text"), item.get("href"))}\n'
        f'{hbold("Цена: ")}${item.get("listing-item__date")}'


        if index%20==0:
            time.sleep(3)

        await message.answer(card)

def main():
    executor.start_polling(dp)

if __name__=='__main__':
    main()