from aiogram import F
from aiogram import Router
from aiogram.types import Message

from filter.admin import AdminFilter
from keyboards.keyboard_admin_panel import admin_panel_keyboard
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message(AdminFilter())
@router.message(F.text == 'Админ-Панель')
async def send_admin_panel(message: Message):
    await message.answer(text=LEXICON_RU['admin_panel'], reply_markup=admin_panel_keyboard)
