from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.main_menu import main_menu_keyboard
from lexicon.lexicon import COMMANDS_RU

router: Router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f'Hello, {message.from_user.username}!', reply_markup=main_menu_keyboard)
    await message.answer(text=COMMANDS_RU['/start'])
