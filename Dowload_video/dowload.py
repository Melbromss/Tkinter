from tkinter import *
from pytube import Youtube
from moviepy.editor import *

def dowload():
    video_path = link.get()
    mp4 = Youtube(video_path).streams.get_highest_resolution().dowload()
    video_clip = VideoFileClip(mp4)
    video_clip.close()
    
display = Tk()
display.title("Youtube Dowloader")
canvas = Canvas(display,width=400,height=200)
canvas.pack()

# ! Name Programe
app_label =Label(display,text="Dowloade Video",font=('Arial',30,'bold'))
canvas.create_window(200,40,window=app_label)

# ! ระบุ link

ll=Label(display,text="Enter URL link")
canvas.create_window(200,80,window=ll)

link= Entry(display,width=80)
canvas.create_window(200,110,window=link)
button = Button(text='Dowloade',command=dowload)
canvas.create_window(200,150,window=button)


display.mainloop()