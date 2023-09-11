from aiogram import F
from aiogram import Router
from aiogram.types import Message

from keyboards.keyboard_main_menu import main_menu_keyboard
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message(F.text == 'Корзина 🛒')
async def send_basket(message: Message):
    await message.answer(text=LEXICON_RU['basket'], reply_markup=main_menu_keyboard)
