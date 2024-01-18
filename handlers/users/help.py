from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (
        "Список команд: ",
        "/start - Начать диалог",
        "/help - Получить справку",
        "/audio - Скачать видео из YouTube и переести в аудио",
        "/video - Скачать видео из YouTube",
    )

    await message.answer("\n".join(text))
