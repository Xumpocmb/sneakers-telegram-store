from aiogram import Router
from aiogram.types import Message

from keyboards.main_menu import main_menu_keyboard
from lexicon.lexicon import COMMANDS_RU

router: Router = Router()


@router.message()
async def cmd_start(message: Message):
    await message.reply(text=COMMANDS_RU['echo'], reply_markup=main_menu_keyboard)
