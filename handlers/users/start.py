import re

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter
from aiogram.utils.deep_linking import get_start_link

from loader import dp
from filters import IsPrivate


@dp.message_handler(CommandStart(deep_link=re.compile(r"\d\d\d")))
async def bot_start_deeplink(message: types.Message):
    deep_link_args = message.get_args()
    await message.answer(f'Привет, {message.from_user.full_name}! \n'
                         f'Вы находитесь в личной переписке \n'
                         f'В вашей команде есть диплинк \n'
                         f'Вы передали аргумент {deep_link_args} \n'
                         )

@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    deep_link = await  get_start_link(payload="123")

    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке\n'
                         f'В вашей команде есть диплинк\n'
                         f'Ваша диплинк ссылка - {deep_link}\n'
                         )