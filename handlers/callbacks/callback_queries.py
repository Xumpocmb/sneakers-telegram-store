from aiogram import F
from aiogram import Router
from aiogram.types import Message, CallbackQuery

from keyboards.main_menu import main_menu_keyboard
from lexicon.lexicon import LEXICON_RU

from bot import bot

router: Router = Router()


@router.callback_query(F.data == 't_shirt')
async def send_t_shirt(callback: CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id, text='t_shirt', reply_markup=main_menu_keyboard)
    await callback.answer()
