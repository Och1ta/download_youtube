from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, bot
from states import DownloadVideo

from pytube import YouTube
import os
import uuid


def dowload_video(url):
    yt = YouTube(url)
    file_id = uuid.uuid4().fields[-1]
    yt.streams.get_highest_resolution().download(
        "download", f"{file_id}.mp4"
    )
    return f"{file_id}.mp4"


@dp.message_handler(Command('video'))
async def start_dow(message: types.Message):
    await message.answer(
        text=f"Привет, {message.from_user.full_name}, "
             f"скинь ссылку на видео."
    )
    await DownloadVideo.download.set()


@dp.message_handler(state=DownloadVideo.download)
async def dowload(message: types.Message, state: FSMContext):
    title = dowload_video(message.text)
    file = open(f'download/{title}', 'rb')
    await message.answer(text="Все скачалось держи видео.")
    try:
        await bot.send_video(message.chat.id, file)
    except:
        await message.answer(text="Файл слишком большой")
    os.remove(f'download/{title}')
    await state.finish()
