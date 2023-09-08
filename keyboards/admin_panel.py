from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

button_1: KeyboardButton = KeyboardButton(text='Добавить товар')
button_2: KeyboardButton = KeyboardButton(text='Удалить товар')
button_3: KeyboardButton = KeyboardButton(text='Начать рассылку')
button_4: KeyboardButton = KeyboardButton(text='Главное меню')


admin_panel_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[
        [
            button_1, button_2, button_3
        ],
        [
            button_4,  # button_5, button_6
        ],
        # [
        #     button_7, button_8, button_9
        # ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
    # one_time_keyboard=True - свернет клавиатуру после использования
)
