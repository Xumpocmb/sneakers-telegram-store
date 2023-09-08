import os

from aiogram import Bot, Dispatcher, Router, types
from settings.bot_menu import set_main_menu
import asyncio
import logging
from dotenv import load_dotenv

from handlers import (
    handler_start,
    handler_echo,
)

logger = logging.getLogger(__name__)
load_dotenv()

# Запуск бота
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    bot: Bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp: Dispatcher = Dispatcher()

    dp.include_routers(
        handler_start.router,
        handler_echo.router,
    )

    # Пропускаем накопившиеся апдейты и запускаем polling
    # start
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        # await send_notify(bot)
        dp.startup.register(set_main_menu)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")