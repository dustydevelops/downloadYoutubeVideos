from tkinter import *
import pytube


def downloadVideo():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.get_highest_resolution()

        video.download('videos')
        notif.config(fg="green", text="Video Download Started")
    except Exception as e:
        e = str('Download Failed:', e)
        notif.config(fg="red", text=(e))


def downloadAudio():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        audio = youtube.streams.get_audio_only()
        audio.download('songs')
        notif.config(fg='green', text='audio download started...')
    except Exception as e:
        e = str('Download Failed:',e)
        notif.config(fg="red", text=(e))

def downloadBoth():
    downloadAudio()
    downloadVideo()
    notif.config(fg='green', text='audio & video downloads have started...')


# Main Screen
master = Tk()
master.title("Youtube Video Downloader")
master.geometry('420x420')

master.config(bg = 'black')

#Create a transparent window
# Labels
Label(master, text="Youtube Video Converter", fg="red", font=("Calibri", 15)).grid(sticky=N, padx=15, row=0)
Label(master, text="Please enter the link to your video below : ", font=("Calibri", 15)).grid(sticky=N, row=1, pady=15)
notif = Label(master, font=("Calibri", 12))
notif.grid(sticky=N, pady=1, row=4)

# Vars
url = StringVar()
# Entr
Entry(master, width=50, textvariable=url).grid(sticky=N, row=2,pady = 15)

# Buttons

Button(master, width=20, text="Download Audio", font=("Calibri", 12), command=downloadAudio).grid(sticky=N, row=3,
                                                                                                  pady=0)
Button(master, width=20, text="Download Video", font=("Calibri", 12), command=downloadVideo).grid(sticky=N, row=3,
                                                                                                  pady=45)
Button(master, width=20, text="Download audio & video", font=("Calibri", 12), command=downloadBoth).grid(sticky=N,
                                                                                                         row=3, pady=90)

master.mainloop()
