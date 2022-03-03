from aiogram import types

from filters import IsPrivate
from loader import dp
from data.config import ADMINS
@dp.message_handler(IsPrivate(), user_id=ADMINS, text="admin")
@dp.message_handler(IsPrivate(), user_id=ADMINS, text="secret")
async  def admin_chat_secret(message: types.Message):
    await  message.answer("Это секретное сообщение, Вызванное одним из администраторов "
                          "в личной переписке")