import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
import start, search
from cleanup import clean_downloads


async def main():
    logging.basicConfig(level=logging.INFO)
    clean_downloads()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(search.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
