from aiogram import F
from aiogram import Router
from aiogram.types import Message


from keyboards.catalog_menu.keyboard_catalog import catalog_keyboard
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message(F.text == 'Каталог 🛍')
async def send_catalog(message: Message):
    await message.answer(text=LEXICON_RU['catalog'], reply_markup=catalog_keyboard)
