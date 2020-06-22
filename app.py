import eel
from pytube import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
import pkg_resources.py2_warn

eel.init('web')

file_size = 0


# @eel.expose()
# def progress_bar(chunk=None, file_handle=None, bytes_remaining=None):
#     file_downloaded = file_size - bytes_remaining
#     percentage = (file_downloaded / file_size) * 100
#     return f'{percentage :00.0f}% done...'

@eel.expose
def start_downloader_thread(url):
    thread = Thread(target=yt_downloader(url))
    thread.start()


def yt_downloader(url):
    global file_size

    try:

        if len(url) == 0:
            showinfo("No URL", "URL is not specified")
            return

        path_to_save = askdirectory()
        if path_to_save is None:
            return

        # creating YouTube object with URL
        yt_object = YouTube(url)

        # Stream is an object which contains video information
        stream_to_be_downloaded = yt_object.streams.get_by_resolution("720p")

        if not stream_to_be_downloaded:
            stream_to_be_downloaded = yt_object.streams.get_highest_resolution()

        file_size = stream_to_be_downloaded.filesize
        stream_to_be_downloaded.download(path_to_save, filename=stream_to_be_downloaded.title)

        showinfo("Downloading Finished", "Downloading Done")

    except Exception as e:
        print(e)
        showinfo("Invalid URL", "Not a valid YouTube URL")


main = Tk()

# set title
main.title("YouTube Downloader")

# set icon
main.iconphoto(False, PhotoImage(file='web/img/cloud-computing.png'))
main.withdraw()
eel.start('index.html', size=(770, 600))
