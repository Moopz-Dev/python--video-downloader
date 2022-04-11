from tkinter import *
from pytube import YouTube
from moviepy.editor import *

root = Tk()
root.title("Video Downloader")
canvas = Canvas(root, width=400, height=200)
canvas.pack()

# commands


def download():
    video_path = link_entry.get()
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    video_clip.close()


# GUI widgets
app_title = Label(root, text="Download Videos",
                  font=("Arial", 20, 'bold'))
canvas.create_window(200, 50, window=app_title)

link_label = Label(root, text="Input link to your video (URL)")
canvas.create_window(200, 80, window=link_label)

link_entry = Entry(root, width=60)
canvas.create_window(200, 100, window=link_entry)

download_button = Button(text="Download", command=download)
canvas.create_window(200, 150, window=download_button)

root.mainloop()
