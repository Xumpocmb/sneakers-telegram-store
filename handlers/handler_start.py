from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.main_menu import main_menu_keyboard
from lexicon.lexicon import LEXICON_RU

from time import sleep

router: Router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f'Hello, {message.from_user.username}!')
    sleep(1.5)
    await message.answer(text=LEXICON_RU['start'], reply_markup=main_menu_keyboard)
