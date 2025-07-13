import base64
from io import BytesIO

from aiogram import types, F, Router, Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiohttp import BasicAuth
from aiohttp.web_fileresponse import content_type

import text
from FusionBrain import FusionBrainAPI
from ai import AI
from aiogram.enums import ParseMode

router = Router()
bot = Bot(token='8053410627:AAHpOkyEvdq8emdJXSou8GAC8ew5FMClQZ4',
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))



class Before:
    def __init__(self, before):
        self.before = before
    def change(self, str):
        self.before = str
    def get(self):
        return self.before

string = Before("")
ai_helper = AI("")

import base64
from io import BytesIO
import os
from aiogram import types, F, Router, Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode
from FusionBrain import FusionBrainAPI
from ai import AI

router = Router()
bot = Bot(token='8053410627:AAHpOkyEvdq8emdJXSou8GAC8ew5FMClQZ4',
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))


class BotState:
    def __init__(self):
        self.current_mode = None

state = BotState()
ai_helper = AI("")

async def sub(mem) -> bool:
        a = str(list(mem)[0]).split("'")
        if a[3] != "left":
            return True
        return False

@router.message(Command("start"))
async def start_handler(msg: Message):
    if sub(await bot.get_chat_member(chat_id=-1001968777247, user_id=msg.from_user.id)):
        kb = [
            [types.KeyboardButton(text="Сделать изображение")],
            [types.KeyboardButton(text="Задать вопрос")]
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True
        )
        await msg.answer("Выберите действие:", reply_markup=keyboard)
    else:
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Подписаться на канал",
            url='https://t.me/daegryo')
        )
        await msg.answer(
            'Для работы с ботом подпишитесь на канал',
            reply_markup=builder.as_markup()
        )



@router.message(F.text == "Сделать изображение")
async def show_menu(message: Message):
    string.before = "image"
    await message.answer(
        text.image,
    )


@router.message(F.text == "Задать вопрос")
async def show_menu(message: Message):
    string.before = "ask"
    await message.answer(
        text.text,
    )

@router.message(F.text)
async def ai(message: Message):
    if string.before == "image":
        api = FusionBrainAPI('https://api-key.fusionbrain.ai/', '33CB1D0903AF9D5768BBECE0728B4B35',
                             '94B842228D5E888E2407186CA29F0F93')
        pipeline_id = api.get_pipeline()
        uuid = api.generate(message.text, pipeline_id)
        files = api.check_generation(uuid)
        # Здесь image_base64 - это строка с данными изображения в формате base64

        image_base64 = files[0]  # Вставьте вашу строку base64 сюда

        # Декодируем строку base64 в бинарные данные

        image_data = base64.b64decode(image_base64)

        # Открываем файл для записи бинарных данных изображения

        with open("image.jpg", "wb") as file:

            file.write(image_data)
        photo = FSInputFile("D:/Work/bot/image.jpg ")
        await message.answer_photo(photo)

    elif string.before == "ask":
        ai_helper.get_prompt(message.text)
        response = ai_helper.give_answer()
        print(type(response))
        if not response or not response.strip():
            response = "Извините, не получилось сформировать ответ"
        await message.answer(response,)





