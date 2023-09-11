from aiogram import F
from aiogram import Router
from aiogram.types import Message

from keyboards.keyboard_main_menu import main_menu_keyboard

router: Router = Router()


@router.message(F.photo)
async def send_sticker(message: Message):
    await message.answer('фото', reply_markup=main_menu_keyboard)
