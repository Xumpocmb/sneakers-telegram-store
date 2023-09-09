from aiogram.fsm.state import StatesGroup, State


class AddItemState(StatesGroup):
    choosing_category_name = State()
    choosing_name = State()
    choosing_description = State()
    choosing_price = State()
    choosing_photo = State()
