from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.main_menu import main_menu_keyboard
from keyboards.admin_main_menu import admin_main_menu_keyboard
from lexicon.lexicon import LEXICON_RU
from filter.admin import AdminFilter

from time import sleep
from bot_db.bot_database import cmd_start_db

router: Router = Router()


@router.message(AdminFilter())
@router.message(Command('start'))
async def cmd_admin_start(message: Message):
    await message.answer(f'Hello, {message.from_user.username}!')
    sleep(1)
    await cmd_start_db(message)
    await message.answer(text=LEXICON_RU['start'], reply_markup=admin_main_menu_keyboard)


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f'Hello, {message.from_user.username}!')
    sleep(1.5)
    await message.answer(text=LEXICON_RU['start'], reply_markup=main_menu_keyboard)
