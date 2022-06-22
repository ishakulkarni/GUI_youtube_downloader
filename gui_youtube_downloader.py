from pytube import YouTube, Channel, Playlist
import os
from tkinter import *

def video_download():
    url = inputobj.get(1.0, END)
    video_caller = YouTube(url)
    print(video_caller.title)
    video_caller.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download()

    done = Label(win, text="Done!", font='ariel 12  bold')
    done.place(x=250, y=400)
    done.after(3000, done.destroy)

def playlist_download():
    url = inputobj.get(1.0, END)
    playlist = Playlist(url)
    print('No. of videos in playlist = %s' %len(playlist.video_urls))
    for video in playlist.videos:
        video.streams.filter(progressive=True, file_extension='mp4'
                            ).order_by('resolution').desc().first().download()
    done = Label(win, text="Done!", font='ariel 12  bold')
    done.place(x=250, y=400)
    done.after(3000, done.destroy)

def audio_download():
    url = inputobj.get(1.0, END)
    video_caller = YouTube(url)
    print(video_caller.title)
    audio = video_caller.streams.filter(only_audio=True).first()

    #destination folder to save file
    destination = 'songs'
    out_file = audio.download(output_path = destination)
    new_name = os.path.splitext(out_file)
    os.rename(out_file, new_name[0]+".mp3")
    done = Label(win, text="Done!", font='ariel 12  bold')
    done.place(x=250, y=400)
    done.after(3000, done.destroy)

def channel_download(): #downloads all videos in channel
    url = inputobj.get(1.0, END)
    channel_videos = Channel(url)
    print(f'Downloading videos by {channel_videos.channel_name}')
    for video in channel_videos.videos:
        video.streams.filter(progressive=True, file_extension='mp4'
                            ).order_by('resolution').desc().first().download()

        print('done!')
    done = Label(win, text="Done!", font='ariel 12  bold')
    done.place(x=250, y=400)
    done.after(3000, done.destroy)

def video_only_download():
    url = inputobj.get(1.0, END)
    video_caller = YouTube(url)
    print(video_caller.title)
    video = video_caller.streams.filter(only_video=True).first()
    out_path = video.download(output_path=video_caller.title)
    new_name = os.path.splitext(out_path)
    os.rename(out_path,new_name[0] + ".mp4")
    done = Label(win, text="Done!", font='ariel 12  bold')
    done.place(x=250, y=400)
    done.after(3000, done.destroy)


win = Tk()
win.geometry('500x500')
win.resizable(0, 0)
win.title('Youtube-Downloader')
Label(win, text='YouTube Downloader', font='arial 20 bold').pack()

cmdtext = "Enter url and click on what to download: \n" \
          "playlist, video, audio, channel, pictureonly\n"
Label(win, text=cmdtext, font='ariel 12 bold').place(x=80, y=50)

inputobj = Text(win, font='ariel 10', height=2, width='40', wrap=WORD, padx=5, pady=5) #object of class Text
inputobj.place(x=100, y=100)

audioButton = Button(win, text='Audio', font='ariel 12', pady=5,
                     command=audio_download, width=6, bg='royal blue1', activebackground='sky blue')
audioButton.place(x=30, y=200)

videoButton = Button(win, text='Video', font='ariel 12', pady=5,
                     command=video_download, width=6, bg='royal blue1', activebackground='sky blue')
videoButton.place(x=230, y=200)

playlistButton = Button(win, text='Playlist', font='ariel 12', pady=5,
                     command=playlist_download, width=6, bg='royal blue1', activebackground='sky blue')
playlistButton.place(x=430, y=200)

channelButton = Button(win, text='channel', font='ariel 12', pady=5,
                     command=channel_download, width=8, bg='royal blue1', activebackground='sky blue')
channelButton.place(x=130, y=300)

pictureButton = Button(win, text='Picture Only', font='ariel 12', pady=5,
                     command=video_only_download, width=10, bg='royal blue1', activebackground='sky blue')
pictureButton.place(x=330, y=300)

win.mainloop()
