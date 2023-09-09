from aiogram import Router
from aiogram.types import Message

from filter.admin import AdminFilter
from keyboards.keyboard_admin_main_menu import admin_main_menu_keyboard
from keyboards.main_menu import main_menu_keyboard
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message(AdminFilter())
@router.message()
async def cmd_admin_echo(message: Message):
    await message.reply(text=LEXICON_RU['echo'], reply_markup=admin_main_menu_keyboard)


@router.message()
async def cmd_echo(message: Message):
    await message.reply(text=LEXICON_RU['echo'], reply_markup=main_menu_keyboard)
