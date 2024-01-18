import logging

from aiogram import executor

from loader import dp
import handlers
from utils.set_bot_commands import set_default_commands


async def main(dispatcher):
    await set_default_commands(dispatcher)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, on_startup=main)
