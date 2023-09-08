import os
import typing
from aiogram.types import Message
from aiogram.filters import Filter
from dotenv import load_dotenv

load_dotenv()


class AdminFilter(Filter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None) -> None:
        self.is_admin = is_admin
        self.admin_ids = os.getenv('ADMINS').split(',')

    async def __call__(self, message: Message) -> bool:
        if self.is_admin is None:
            return False
        return message.from_user.id in self.admin_ids
