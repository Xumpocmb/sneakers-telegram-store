from aiogram import F
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboard_main_menu import main_menu_keyboard
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message(Command('contacts'))
async def cmd_contacts(message: Message):
    await message.answer(text=LEXICON_RU['contacts'], reply_markup=main_menu_keyboard)


@router.message(F.text == 'Контакты ✉️')
async def send_contacts(message: Message):
    await message.answer(text=LEXICON_RU['contacts'], reply_markup=main_menu_keyboard)
