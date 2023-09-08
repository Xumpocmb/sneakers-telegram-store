from aiogram import F
from aiogram import Router
from aiogram.types import Message


from keyboards.main_menu import main_menu_keyboard
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message(F.text == 'Каталог 🛍')
async def send_catalog(message: Message):
    await message.answer(text=LEXICON_RU['catalog'], reply_markup=main_menu_keyboard)
