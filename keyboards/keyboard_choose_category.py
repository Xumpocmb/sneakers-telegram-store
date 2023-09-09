from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

button_1: KeyboardButton = KeyboardButton(text='Майки')
button_2: KeyboardButton = KeyboardButton(text='Шорты')
button_3: KeyboardButton = KeyboardButton(text='Жопа друга')
button_4: KeyboardButton = KeyboardButton(text='Кроссовки')
button_5: KeyboardButton = KeyboardButton(text='Полуботинки')
button_6: KeyboardButton = KeyboardButton(text='Ботинки')


choose_category_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[
        [
            button_1, button_2, button_3
        ],
        [
            button_4, button_5, button_6
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите категорию..',
)
