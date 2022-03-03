import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import banned_users


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info("---------------------Update------------")
        logging.info("---------------------1. preprocess Update------------")
        logging.info("---------------------Next step------------")
        data["middleware_data"] = 'it will go until post process update'

        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.message.callback_query.id.from_user.id
        else:
            return
        if user in banned_users:
            raise CancelHandler()
