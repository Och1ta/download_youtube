import os

import pytube
import telebot
from dotenv import load_dotenv
from win32comext.shell import shell, shellcon

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


@bot.message_handler(content_types=['text'])
def download_video(message):
    bot.send_message(message.chat.id, text="Ссылка получена")

    try:
        youtubelink = pytube.YouTube(message.text)
        video = youtubelink.streams.get_highest_resolution()
        video.download(
            output_path=shell.SHGetKnownFolderPath(
                shellcon.FOLDERID_Downloads
            )
        )
        print(shell.SHGetKnownFolderPath(shellcon.FOLDERID_Downloads))
        bot.send_message(
            message.chat.id,
            text=f"Готово загрузка завершена файл находится по пути:\n"
                 f"{shell.SHGetKnownFolderPath(shellcon.FOLDERID_Downloads)}"
        )
    except:
        bot.send_message(message.chat.id, text="Ошибка. Проверьте ссылку")


bot.polling(none_stop=True)
