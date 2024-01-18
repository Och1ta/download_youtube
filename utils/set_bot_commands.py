from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand(
                command="start",
                description="Запустить бота"
            ),
            types.BotCommand(
                command="help",
                description="Вывести справку"
            ),
            types.BotCommand(
                command="audio",
                description="Скачать видео из YouTube и переести в аудио"
            ),
            types.BotCommand(
                command="video",
                description="Скачать видео из YouTube"
            )
        ]
    )
