import pytube
from aiogram import Router
from dotenv import load_dotenv
from win32comext.shell import shell, shellcon

router = Router()

load_dotenv()


@router.message()
async def download_video(message):
    try:
        youtubelink = pytube.YouTube(message.text)
        video = youtubelink.streams.get_highest_resolution()
        video.download(
            output_path=shell.SHGetKnownFolderPath(
                shellcon.FOLDERID_Downloads
            )
        )
    except:
        await message.reply(text="Ошибка. Проверьте ссылку")
