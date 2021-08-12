import youtube_dl
import os
import tkinter as tk
from tkinter import messagebox
import threading
import sys

filename = ""

window = tk.Tk()
window.title("Youtube to MP3")
window.resizable(False, False)
window.geometry("400x110+483+329")

label = tk.Label(text="Enter the Youtube URL to Download:")
label.pack(fill=tk.BOTH)

text_input = tk.Entry(width=40)
text_input.pack(fill=tk.BOTH, padx=5)


def handle_download():

    global filename
    # get URL from text input
    if text_input.get() == "":
        messagebox.showerror("Error", "URL is empty")
        return

    try:
        # create youtube download object
        video_url = text_input.get()
        video_info = youtube_dl.YoutubeDL().extract_info(video_url, False)
    except Exception as e:
        messagebox.showerror("Error", "URL is invalid")
        return

    # retrive filename from youtube class object
    filename = f"{video_info['title']}.mp3"

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    messagebox.showinfo(title="Download MP3 Successfully",
                        message=f"Download {filename} completed")
    return

def start_download():
	thread = threading.Thread(target=handle_download)
	thread.start()
	return

def open_folder():
    os.startfile("")
    return


btn_get_mp3 = tk.Button(text="Download MP3", command=start_download)
btn_get_mp3.pack(fill=tk.BOTH, pady=5, padx=5)

btn_get_mp3 = tk.Button(text="Open Folder", command=open_folder)
btn_get_mp3.pack(fill=tk.BOTH, pady=5, padx=5)


window.mainloop()
