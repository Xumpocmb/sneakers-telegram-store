from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

button_1: KeyboardButton = KeyboardButton(text='Отмена')

cancel_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[
        [
            button_1,
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..',
    one_time_keyboard=True,
)
