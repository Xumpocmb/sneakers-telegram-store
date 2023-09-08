from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)


button_1: InlineKeyboardButton = InlineKeyboardButton(text='Майки', callback_data='t_shirt')
button_2: InlineKeyboardButton = InlineKeyboardButton(text='Шорты', callback_data='shorts')
button_3: InlineKeyboardButton = InlineKeyboardButton(text='Жопа друга', callback_data='ass')
button_4: InlineKeyboardButton = InlineKeyboardButton(text='Кроссовки', callback_data='sneakers')
button_5: InlineKeyboardButton = InlineKeyboardButton(text='Полуботинки', callback_data='low_shoes')
button_6: InlineKeyboardButton = InlineKeyboardButton(text='Ботинки', callback_data='boots')


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
