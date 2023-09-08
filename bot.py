import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import (
    handler_start,
    handler_sticker,
    handler_photo,
    handler_contacts,
    handler_basket,
    handler_catalog,
    handler_admin_panel,

    handler_echo,
)
from settings.bot_menu import set_main_menu
from  bot_db.bot_database import db_start

logger = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)

load_dotenv()
bot: Bot = Bot(token=os.getenv('BOT_TOKEN'))
dp: Dispatcher = Dispatcher()


# Запуск бота
async def main():

    logger.info("Starting bot")

    dp.include_routers(
        handler_start.router,
        handler_sticker.router,
        handler_photo.router,
        handler_contacts.router,
        handler_basket.router,
        handler_catalog.router,
        handler_admin_panel.router,

        handler_echo.router,
    )

    # Пропускаем накопившиеся апдейты и запускаем polling
    # start
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        # await send_notify(bot)
        dp.startup.register(set_main_menu)
        await db_start()
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
