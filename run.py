from aiogram import Dispatcher, Bot

from config import BOT_TOKEN

from handler.start import router

import asyncio 
import sys
import logging

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

try:
    if __name__ == "__main__":
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
except KeyboardInterrupt:
    print("Bot was stopped! ExitTag: KeyboardInterrupt")
except SystemExit:
    print("Bot was stopped! ExitTag: SystemExit")
