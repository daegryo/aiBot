from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Filter, Command
from aiogram.types import Update, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
import logging
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession
from aiohttp import BasicAuth

import config
from handlers import router, bot



#bot = Bot(token='6949718238:AAFAxK_0kfb1lbcvJC6Rfqf4NsTnxxe1OiQ', parse_mode=ParseMode.HTML)


async def main():
 #   auth = BasicAuth(login='daryaalbertovna', password='790089910040')
  #  session = AiohttpSession(proxy=('http://proxy.server:3128', auth))

  #  bot = Bot(token='6949718238:AAFAxK_0kfb1lbcvJC6Rfqf4NsTnxxe1OiQ',session=session, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())