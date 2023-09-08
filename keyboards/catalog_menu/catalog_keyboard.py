from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)


button_1: InlineKeyboardButton = InlineKeyboardButton(text='Майки', callback_data='go_to_stage2')
button_2: InlineKeyboardButton = InlineKeyboardButton(text='Шорты', callback_data='go_to_stage2')
button_3: InlineKeyboardButton = InlineKeyboardButton(text='Жопа друга', callback_data='go_to_stage2')
button_4: InlineKeyboardButton = InlineKeyboardButton(text='Кроссовки', callback_data='go_to_stage2')
button_5: InlineKeyboardButton = InlineKeyboardButton(text='Полуботинки', callback_data='go_to_stage2')
button_6: InlineKeyboardButton = InlineKeyboardButton(text='Ботинки', callback_data='go_to_stage2')


catalog_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            button_1, button_2, button_3
        ],
        [
            button_4, button_5, button_6
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
)
