from aiogram import F
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from filter.admin import AdminFilter
from keyboards.keyboard_admin_main_menu import admin_main_menu_keyboard
from keyboards.keyboard_cancel import cancel_keyboard
from keyboards.keyboard_choose_category import choose_category_keyboard
from states.add_item_states import AddItemState
from bot_db.bot_database import db_add_item

router: Router = Router()

available_categories = ['Майки', 'Шорты', ]


@router.message(F.text == 'Отмена')
async def choosing_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.reply('Создание товара отменено!', reply_markup=admin_main_menu_keyboard)


@router.message(AdminFilter())
@router.message(F.text == 'Добавить товар')
async def choosing_category_state(message: Message, state: FSMContext):
    await state.set_state(AddItemState.choosing_category_name)
    await message.answer('Укажите категорию товара!', reply_markup=choose_category_keyboard)


@router.message(AddItemState.choosing_category_name, F.text.in_(available_categories))
async def choosing_name_state(message: Message, state: FSMContext):
    await state.update_data(category=message.text.lower())
    await state.set_state(AddItemState.choosing_name)
    await message.answer('Укажите название товара!', reply_markup=cancel_keyboard)


@router.message(AddItemState.choosing_name)
async def choosing_description_state(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AddItemState.choosing_description)
    await message.answer('Укажите описание товара!', reply_markup=cancel_keyboard)


@router.message(AddItemState.choosing_description)
async def choosing_price_state(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(AddItemState.choosing_price)
    await message.answer('Укажите цену товара!', reply_markup=cancel_keyboard)


@router.message(AddItemState.choosing_price)
async def choosing_photo_state(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(AddItemState.choosing_photo)
    await message.answer('Пришлите фото товара!', reply_markup=cancel_keyboard)


@router.message(lambda message: not message.photo, AddItemState.choosing_photo)
async def photo_not_found(message: Message):
    await message.reply('Это не фото!')


@router.message(F.photo, AddItemState.choosing_photo)
async def finish_state(message: Message, state: FSMContext):
    await state.update_data(photo=message.text)
    userdata = await state.get_data()
    await db_add_item(userdata)
    await message.answer('Товар успешно создан!', reply_markup=admin_main_menu_keyboard)
    await state.clear()
