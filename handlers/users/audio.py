from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, bot
from states import DownloadAudio

from pytube import YouTube
import os
import uuid


def dowload_audio(url):
    yt = YouTube(url)
    file_id = uuid.uuid4().fields[-1]
    yt.streams.filter(only_audio=True).first().download(
        "download", f"{file_id}.mp3"
    )
    return f"{file_id}.mp3"


@dp.message_handler(Command('audio'))
async def start_dow(message: types.Message):
    await message.answer(
        text=f"Привет, {message.from_user.full_name}, "
             f"скинь ссылку на видео и я отправлю ее тебе ввиде аудио."
    )
    await DownloadAudio.download.set()


@dp.message_handler(state=DownloadAudio.download)
async def dowload(message: types.Message, state: FSMContext):
    title = dowload_audio(message.text)
    file = open(f'download/{title}', 'rb')
    await message.answer(text="Все скачалось держи аудио")
    try:
        await bot.send_audio(message.chat.id, file)
    except:
        await message.answer(text="Файл слишком большой")
    os.remove(f'download/{title}')
    await state.finish()
